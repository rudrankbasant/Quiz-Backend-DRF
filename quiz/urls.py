from django.urls import path
from .views import Quiz, RandomQuestion, QuizQuestions

app_name = 'quiz'

urlpatterns = [
    path('',  Quiz.as_view(), name='quiz'),
    path('r/<str:topic>/', RandomQuestion.as_view(), name='random-question'),
    path('q/<str:topic>/', QuizQuestions.as_view(), name='quiz-questions')
]
