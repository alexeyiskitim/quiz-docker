from django.forms import ModelForm
from django import forms
from quiz_app.models import Quiz, QuestionType, Question, Result, OptionToAnswer

class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'

class QuestionTypeForm(ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'

class QuestionForm(ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'

class QuizQuestionResultForm(ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'
