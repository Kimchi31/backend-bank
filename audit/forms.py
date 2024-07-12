# from django.db import models
# from django import forms


# class AuditForm(forms.ModelForm):
#     name = models.CharField(label='Student name',max_length= 100)
#     class Meta:
#         model = models
#         fields = '__all__'
#         request = 'POST'


# class AuditModelForm(forms.ModelForm):
#     class Meta:
#         model = models
#         fields = '__all__'
#


# from django import forms
# from .models import Plan
#
# class AuditForm(forms.ModelForm):
#     class Meta:
#         model = Plan
#         fields = ['name', 'departament', 'brief_description', 'reccomendations',
#                   'action_to_implement_the_recommendation', 'form_of_completion', 'deadline',
#                   'completed', 'expired', 'not_done', 'removed_from_control', 'rescheduled']
#         widgets = {
#             'completed': forms.CheckboxInput(),
#             'expired': forms.CheckboxInput(),
#             'not_done': forms.CheckboxInput(),
#             'removed_from_control': forms.CheckboxInput(),
#             'rescheduled': forms.CheckboxInput(),
#         }









from django import forms
from .models import Department
class ExcelForm(forms.Form):
    excel_file = forms.FileField(label='Файл Excel', required=True)
    departament = forms.ModelChoiceField(queryset=Department.objects.all(), label='Наименование подразделения')
    brief_description = forms.CharField(label='Краткое описание обнаружения', max_length=100)
    reccomendations = forms.CharField(label='Рекомендация подразделения внутреннего аудита', max_length=1000)
    action_to_implement_the_recommendation = forms.CharField(label='Мероприятие по исполнению рекомендации подразделения внутреннего аудита', max_length=1000)
    form_of_completion = forms.CharField(label='Форма завершения', max_length=100)
    deadline = forms.DateTimeField(label='Срок исполнения',widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    completed = forms.BooleanField(label='Выполнено', required=False)
    completed = forms.BooleanField(label='Выполнено', required=False)
    expired = forms.BooleanField(label='Выполнено не в установленный срок', required=False)
    not_done = forms.BooleanField(label='Не выполнено', required=False)
    removed_from_control = forms.BooleanField(label='Снято с контроля', required=False)
    rescheduled = forms.BooleanField(label='Перенесено', required=False)






from .models import Plan

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'




from django.shortcuts import render, redirect
from .forms import ExcelForm, PlanForm

def upload_excel(request):
    if request.method == 'POST':
        excel_form = ExcelForm(request.POST, request.FILES)
        if excel_form.is_valid():
            plan_form = PlanForm(excel_form.cleaned_data)
            if plan_form.is_valid():
                plan_form.save()
                return redirect('some_view_name')
    else:
        excel_form = ExcelForm()
    return render(request, 'upload_excel.html', {'excel_form': excel_form})



