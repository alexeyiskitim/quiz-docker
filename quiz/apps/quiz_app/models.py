from django.db import models

# Опрос: название, дата старта, дата окончания, описание.
class Quiz(models.Model):
    name = models.CharField ('Название', max_length = 200, unique = True, db_index= True)
    date_start = models.DateTimeField ('Дата старта', auto_now_add=True, editable=False)
    date_end = models.DateTimeField ('Дата окончания')
    description = models.CharField ('Описание', max_length = 10000, unique = True, db_index= True)

    def __str__(self):
        return self.name

# Тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)
class QuestionType(models.Model):
    type = models.CharField ('Тип вопроса', max_length = 200, unique = True)

    def __str__(self):
        return self.type


# Вопрос: Опрос FK, текст вопроса, тип вопроса FK
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    text = models.CharField ('Текст вопроса', max_length = 200, db_index= True)
    type = models.ForeignKey(QuestionType, on_delete = models.CASCADE)

    def __str__(self):
        return self.text  + "  (тип вопроса: '" + self.type.type + "')"

# Список возможных ответов на вопрос: Вопрос FK, Текст, Признак корректный
class OptionToAnswer(models.Model):
    text = models.CharField ('Вариант ответа', max_length = 200, unique = True, db_index= True)
    isCorrect = models.BooleanField('Корректный ответ')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text + "  (на вопрос: '" + self.question.text + "')"

# Результат опроса: Вопрос FK, Опрос FK, User ID
class Result(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_to_answer = models.ForeignKey(OptionToAnswer, on_delete=models.CASCADE)  #ответ для варианта ответа QuestionType.id=2 или 3. Для 2 нужно добавить валидацию что можно выбрать только один вариант ответа
    textAnswer = models.CharField('Ответ', default='', max_length=200, db_index=True, null=True, blank=True)  # ответ для варианта ответа QuestionType.id=1
    user_id = models.PositiveIntegerField('ID пользователя', null=False)

    def __str__(self):
        return self.question.text

    class Meta:
        unique_together = (('question', 'user_id', 'option_to_answer'),)

