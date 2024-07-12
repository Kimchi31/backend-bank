from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=1000, verbose_name='Наименование подразделения')

    def __str__(self):
        return self.name


class Plan(models.Model):
    departament = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Наименование подразделения')
    brief_description = models.TextField(verbose_name='Краткое описание обнаружения')
    reccomendations = models.TextField(verbose_name='Рекоменлации подраздлеления внутреннего аудита')
    action_to_implement_the_recommendation = models.TextField(verbose_name='Мероприятие по исполнению рекомендации подразделения внутреннего аудита')
    form_of_completion = models.CharField(max_length=250, verbose_name='Форма завершения')
    deadline = models.DateTimeField(auto_now=False, verbose_name='Срок исполнения')

    completed = models.BooleanField(default=False, verbose_name='Выполнено')
    expired = models.BooleanField(default=False, verbose_name='Выполнено не в установленный срок')
    not_done = models.BooleanField(default=False, verbose_name='Не выполнено')
    removed_from_control = models.BooleanField(default=False, verbose_name='Снято с контроля')
    rescheduled = models.BooleanField(default=False, verbose_name='Перенесено')

