from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:quiz_id>/", views.quiz, name="quiz"),
    path("<int:quiz_id>/question/<int:question_id>/", views.question, name="question"),
    path("<int:quiz_id>/score", views.score, name="score"),
]