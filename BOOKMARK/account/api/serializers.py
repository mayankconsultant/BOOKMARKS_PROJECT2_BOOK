from employees.models import *
from rest_framework import serializers

from ..models import Employee


class detailSerializer(serializers.ModelSerializer):
    class Meta:
        model = employeedetails
        fields = ('gender', 'nationality')


class EmployeeSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format='%d-%b-%Y')
    details = detailSerializer

    class Meta:
        model = Employee
        fields = ('username', 'empNo', 'employeetype', 'email', 'first_name', 'last_name', 'get_name', 'get_gender',
                  'date_joined', 'id', 'get_department')

        # ORIGINAL  WORKING FINE

        # class EmployeeSerializer(serializers.ModelSerializer):
        #     date_joined = serializers.DateTimeField(format='%d-%b-%Y')
        #
        #     class Meta:
        #         model = Employee
        #         fields = (
        #         'username', 'empNo', 'employeetype', 'email', 'first_name', 'last_name', 'get_name', 'date_joined',
        #         'id')
