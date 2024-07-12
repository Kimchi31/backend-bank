from django.shortcuts import render
from .forms import ExcelForm
from django.shortcuts import render, redirect
from .models import Department, Plan

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
import logging

from rest_framework import viewsets
from .serializers import PlanSerializer

from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from docx import Document
from io import BytesIO







def report(request):
    print('request')
    return HttpResponse("success", status.HTTP_200_OK)

class ReportViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Plan.objects.all()
        serializer = PlanSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Plan.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = PlanSerializer(user)
        return Response(serializer.data)

    # def create(self, request):
    #     data = request.data
    #     department_id = data.get('department_id')
    #     department = Department.objects.get(id=department_id) if department_id else None
    #
    #     serializer = PlanSerializer(data=request.data)
    #     logging.warning(serializer)
    #     if serializer.is_valid():
    #         serializer.save(department=department)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        data = request.data
        department_id = data.get('department')

        department = Department.objects.get(id=department_id)
        logging.warning(department)
        data['departament'] = department.id
        serializer = PlanSerializer(data=data)

        logging.warning(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def index(request):

    if request.method == 'POST':
        form = ExcelForm(request.POST, request.FILES)
        if form.is_valid():
            departament = form.cleaned_data['departament']
            brief_description = form.cleaned_data['brief_description']
            reccomendations = form.cleaned_data['reccomendations']
            action_to_implement_the_recommendation = form.cleaned_data['action_to_implement_the_recommendation']
            form_of_completion = form.cleaned_data['form_of_completion']
            deadline = form.cleaned_data['deadline']
            completed = form.cleaned_data['completed']
            expired = form.cleaned_data['expired']
            not_done = form.cleaned_data['not_done']
            removed_from_control = form.cleaned_data['removed_from_control']
            rescheduled = form.cleaned_data['rescheduled']


            plan = Plan.objects.create(
                departament=departament,
                brief_description=brief_description,
                reccomendations=reccomendations,
                action_to_implement_the_recommendation=action_to_implement_the_recommendation,
                form_of_completion=form_of_completion,
                deadline=deadline,
                completed=completed,
                expired=expired,
                not_done=not_done,
                removed_from_control=removed_from_control,
                rescheduled=rescheduled
            )

            return render(request, "succsess.html")
    else:
        form = ExcelForm()
    return render(request, 'index.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('some_view_name')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer





