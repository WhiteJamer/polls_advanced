from django.db import models
from django.conf import settings

class Poll(models.Model):
    name = models.CharField(max_length=255, help_text='Название')
    start_date = models.DateTimeField(auto_now_add=True, help_text='Дата старта') # Указывается настоящее дата и время.
    end_date = models.DateTimeField(blank=True, null=True, help_text='Дата окончания') # Возможность не указывать дату окончания. (в тз не было указано ничего на этот счет, вот я и решил, что так лучше)
    description = models.TextField(blank=True, null=True, help_text='Описание')
    is_active = models.BooleanField(default=True, help_text='Активен?')

    def __str__(self):
        return f"{self.name}"


class Question(models.Model):
    TYPE_TEXT = 'TEXT'
    TYPE_CHOICE_ONE = 'ONE'
    TYPE_CHOICE_MANY = 'MANY'

    QUESTION_TYPES = (
        (TYPE_TEXT, 'Ответ текстом'),
        (TYPE_CHOICE_ONE, 'Выбор одного варианта'),
        (TYPE_CHOICE_MANY, 'Выбор несколький вариантов'),
    )

    text = models.TextField(help_text='Текст вопроса')
    type = models.CharField(max_length=4, choices=QUESTION_TYPES, help_text='Тип вопроса')
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='questions', help_text='Опрос')

    def __str__(self):
        return f"[{self.get_type_display()}] - {self.text}"

class Option(models.Model): # Вариант ответа
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options', help_text='Вопрос')
    text = models.TextField(help_text='Текст варианта')

    def __str__(self):
        return self.text

class Answer(models.Model): # Модель для хранения ответов пользователей
    text = models.TextField(help_text='Текст ответа')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='answers', help_text='Владелец')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers', help_text='Вопрос')

    def __str__(self):
        return self.text


