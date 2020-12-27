from django.conf import settings
from employees.models import employee_resources, teams, department
from rest_framework import serializers

user = settings.AUTH_USER_MODEL


class EmpResSerializer(serializers.ModelSerializer):
    # employeeid = serializers.RelatedField(source=user, read_only=True)

    assigned_date = serializers.DateTimeField(format='%d-%b-%Y', required=False)
    deassigned_date = serializers.DateTimeField(format='%d-%b-%Y', required=False)

    class Meta:
        model = employee_resources
        # fields = ['resource_id','resource_type','assigned_date','deassigned_date','deassigned_comments','id','employeeid']
        fields = "__all__"
    # def create(self, validated_data):


class teamsSer(serializers.ModelSerializer):
    class Meta:
        model = teams
        fields = "__all__"


class departmentSer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields = "__all__"
