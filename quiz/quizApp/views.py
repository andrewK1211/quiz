from django.shortcuts import get_object_or_404, render

from .models import Quiz, Question, Choice

# Create your views here.

def index(request):
    latest_quiz_list = Quiz.objects.order_by("id")[:10]
    context = {"latest_quiz_list": latest_quiz_list,}
    return render(request, "quizApp/index.html", context)

def quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    first_question = Question.objects.filter(quiz = quiz).order_by("order").first()
    context = {"quiz": quiz, "first_question": first_question}
    return render(request, "quizApp/quiz.html", context)

def question(request, quiz_id, question_id):
    update_score(request)

    quiz = get_object_or_404(Quiz, pk=quiz_id)
    question = get_object_or_404(Question, pk=question_id)
    last_question = Question.objects.filter(quiz = quiz).order_by("order").last()
    is_last_question = last_question == question
    next_question = None

    if (not is_last_question):
        next_question = Question.objects.filter(quiz = quiz).filter(order = question.order + 1).first()
    
    if (question.order == 0):
        request.session['score'] = 0

    context = {"quiz": quiz, "question": question, "next_question": next_question, "is_last_question": is_last_question}
    return render(request, "quizApp/question.html", context)

def score(request, quiz_id):
    score = update_score(request)

    quiz = get_object_or_404(Quiz, pk=quiz_id)
    total = Question.objects.filter(quiz = quiz).count()
    context = {"quiz": quiz, "score": score, "total": total}
    return render(request, "quizApp/score.html", context)

def update_score(request):
    if request.method == 'POST':
        choice = get_object_or_404(Choice, pk=request.POST.get('choice'))
        current_score = request.session['score']
        if choice.correct_answer:
            request.session['score'] = current_score + 1
            return current_score + 1
        else:
            return current_score