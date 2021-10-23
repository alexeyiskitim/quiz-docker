from rest_framework import serializers
from quiz_app.models import Quiz, QuestionType, Question, Result, OptionToAnswer

#ОПРОС
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


#ВОПРОС
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionType
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

#Вопрос с типом вопроса
class QuestionDetailedSerializer(serializers.ModelSerializer):
    type = QuestionTypeSerializer(read_only = False)

    class Meta:
        model = Question
        fields = '__all__'

#Опрос с детализацией по вопросу и типу вопроса
class QuizDetailedSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(read_only=False)
    type = QuestionTypeSerializer(read_only = False)
    class Meta:
        model = Question
        fields = '__all__'

#   РЕЗУЛЬТАТЫ
#Выдача/запись результатов
class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'


class ResultDetailedSerializer(serializers.ModelSerializer):
    question = QuizDetailedSerializer(read_only=False)

    class Meta:
        model = Result
        fields = '__all__'
