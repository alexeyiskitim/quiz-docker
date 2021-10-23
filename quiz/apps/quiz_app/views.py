from django.shortcuts import render
from .models import Quiz, QuestionType, Question, Result, OptionToAnswer
from .serializers import QuizSerializer, QuestionSerializer, QuestionSerializer, ResultSerializer, QuestionTypeSerializer, QuestionDetailedSerializer, QuizDetailedSerializer, ResultDetailedSerializer
from .forms import QuizForm, QuestionTypeForm, QuestionForm, QuizQuestionResultForm
from rest_framework import generics, permissions, viewsets, status, serializers
from rest_framework.response import Response


# REST FRAMEWORK
# ОПРОСЫ
class QuizCreateView(generics.CreateAPIView):               #создание опроса
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticated]      #необходим токен для админа согласно требованию

class QuizView(generics.RetrieveUpdateDestroyAPIView):      #просмотр/редактирование/удаление опроса
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    permission_classes = [permissions.IsAuthenticated]      #необходим токен для админа согласно требованию

class QuizListView(generics.ListAPIView):                   #просмотр списка опросов
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

# ВОПРОСЫ
class QuestionCreateView(generics.CreateAPIView):           #создание вопроса опросника
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]      #необходим токен для админа согласно требованию

class QuestionView(generics.RetrieveUpdateDestroyAPIView):  #просмотр/редактирование/удаление вопроса опросника
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [permissions.IsAuthenticated]      #необходим токен для админа согласно требованию

class QuestionListView(viewsets.ModelViewSet):              #просмотр списка вопросов
    serializer_class = QuestionDetailedSerializer
    queryset = Question.objects.all()


class QuizListView(viewsets.ModelViewSet):                  #просмотр списка опросов c детализцией по вопросам
    serializer_class = QuizDetailedSerializer
    queryset = Question.objects.all()


class ResultCreateView(generics.CreateAPIView):                  #создание результата
    serializer_class = ResultSerializer

    def create(self, request, *args, **kwargs):
        """
        Метод который проверяет json
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        question_type_id = Question.objects.get(id=request.data['question']).type.id
        if question_type_id == 1:   #тип вопроса - ответ текстом
            if request.data['textAnswer']:
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                raise serializers.ValidationError('textAnswer не может быть пустым для типа вопроса 1 - "ответ текстом"')
                Response(serializer.data, status=status.HTTP_400_BAD_REQUEST, headers=headers)
        elif question_type_id == 3: #3 - Ответ с выбором нескольких вариантов
            request.data['textAnswer'] = ""
            Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        elif question_type_id == 2: #2 - Ответ с выбором одного варианта
            question_id = Result.objects.filter(question=request.data['question'],user_id=request.data['user_id']).first().id
            if question_id:
                raise serializers.ValidationError('У этого вопроса может быть только один вариант ответа')
                Response(serializer.data, status=status.HTTP_400_BAD_REQUEST, headers=headers)
            else:
                request.data['textAnswer'] = ""
                Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ResultView(viewsets.ModelViewSet):                  #просмотр результатов по UserId
    serializer_class = ResultDetailedSerializer
#    queryset = Result.objects.all()

    def get_queryset(self):
        queryset = Result.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        if user_id:
            return Result.objects.filter(user_id=user_id)
        else:
            return Result.objects.all()
    print("get")