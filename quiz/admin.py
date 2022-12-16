from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]

@admin.register(models.Quizzes)

class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ]

class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer_text',
        'is_correct',
    ]

@admin.register(models.Question)

class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'quiz',
        'question_text',
    ]
    list_display = [
        'id',
        'question_text',
        'quiz',
        'date_created',
    ]
    inlines = [
        AnswerInlineModel
    ]

@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text',
        'question',
        'is_correct',
    ]



