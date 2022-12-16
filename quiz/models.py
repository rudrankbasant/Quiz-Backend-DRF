from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ['id']

    def __str__(self):
        return self.name  

class Quizzes(models.Model):

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ['id']

    title = models.CharField(max_length=200, default =  _('New Quiz'), verbose_name=_('Quiz Title'))
    category = models.ForeignKey(Category, default = 1, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.title       

class Updated(models.Model):
    date_updated = models.DateTimeField(verbose_name = _("Last Updated"), auto_now=True)
    
    class Meta:
        abstract = True

class Question(Updated):

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']

    SCALE = (
        (0, _('Easy')),
        (1, _('Medium')),
        (2, _('Hard')),
    )    

    TYPE = (    
        (0, _('Multiple Choice')),
        (1, _('True or False')),
        (2, _('Fill in the Blanks')),
        (3, _('Essay')),
    )   

    quiz = models.ForeignKey(Quizzes, related_name='question', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    question_type = models.IntegerField(choices=TYPE, default=0)
    difficulty = models.IntegerField(choices=SCALE, default=0)
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Date Created')
    )
    is_active = models.BooleanField(default=False, verbose_name=_("Active Status"))

    def __str__(self):
        return self.question_text

class Answer(Updated):
    question = models.ForeignKey(Question, related_name="answer", on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200, verbose_name=_("Answer Text"))
    is_correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']

    def __str__(self):
        return self.answer_text     
