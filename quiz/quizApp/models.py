from django.db import models

# Create your models here.

class Quiz(models.Model):
    quiz_name = models.CharField(max_length=200)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    order = models.IntegerField()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    correct_answer = models.BooleanField()