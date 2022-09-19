from rest_framework import serializers
from employees.models import EmployeesModel


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeesModel
        fields = "__all__"
