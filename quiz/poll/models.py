from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    start_date = models.DateField(editable=False, verbose_name="Дата начала")
    end_date = models.DateField(editable=True, verbose_name="Дата окончания")
    description = models.TextField(blank=True, verbose_name="Описание опроса")

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plurar = "Опросы"

    def __str__(self):
        return self.title


class Question(models.Model):
    QUESTION_TYPE = (
        (1, "Выбор одного варианта"),
        (2, "Выбор нескольких вариантов"),
        (3, "Ответ текстом"),
    )
    poll = models.ForeignKey(Poll, verbose_name="Опрос")
    question = models.TextField(max_length=2000, verbose_name="Текст вопроса")
    question_type = models.CharField(
        max_length=1, choices=QUESTION_TYPE, default=1, verbose_name="Тип вопроса"
    )

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plurar = "Вопросы"

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plurar = "Ответы"

    def __str__(self):
        return self.answer
