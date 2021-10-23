from django.contrib import admin
from .models import Quiz, Question, QuestionType, Result, OptionToAnswer

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(QuestionType)
admin.site.register(Result)
admin.site.register(OptionToAnswer)