#quiz_app urls.py
from django.urls import path
from quiz_app.views import *

app_name = 'quiz_app'
urlpatterns = [
#   REST API
#   ОПРОСЫ
    path('api/v1/quiz/create', QuizCreateView.as_view(), name='QuizCreateView'),    #создание опроса
    path('api/v1/quiz/<int:pk>/', QuizView.as_view(), name='QuizView'),             #просмотр/редактирование/удаление опроса
#    path('api/v1/quiz/all', QuizListView.as_view(), name='QuizListView'),           #список опросов
#   ВОПРОСЫ
    path('api/v1/question/create', QuestionCreateView.as_view(), name='QuestionCreateView'),          #создание вопроса опросника
    path('api/v1/question/<int:pk>/', QuestionView.as_view(), name='QuestionView'),                   #просмотр/редактирование/удаление вопроса опросника
    path('api/v1/question/all/', QuestionListView.as_view({'get':'list'}), name='QuestionListView'),  #список вопросов c типом вопроса
    path('api/v1/quiz/all/', QuizListView.as_view({'get':'list'}), name='QuizListView'),  #список вопросов c типом вопроса
#   РЕЗУЛЬТАТЫ
    path('api/v1/question_result/create', ResultCreateView.as_view(), name='ResultCreateView'),
    path('api/v1/question_result/all/', ResultView.as_view({'get': 'list'}), name='ResultView'),
]




#    path('api/v1/quiz/all', QuestionnaireListView.as_view(), name='QuestionnaireListView'),