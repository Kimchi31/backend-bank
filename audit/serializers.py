from rest_framework import serializers
from .models import Plan, Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name']


class PlanSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source='departament.name', read_only=True)

    class Meta:
        model = Plan
        fields = [
            'id',
            'department_name',
            'brief_description',
            'reccomendations',
            'action_to_implement_the_recommendation',
            'form_of_completion',
            'deadline',
            'completed',
            'expired',
            'not_done',
            'removed_from_control',
            'rescheduled'
        ]










