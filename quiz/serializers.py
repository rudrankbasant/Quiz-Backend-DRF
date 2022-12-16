from rest_framework import serializers
from .models import Quizzes, Question

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields = [
            'title'
        ]

class RandomQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'question_text'
        ]

class QuizQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'question_text'
        ]