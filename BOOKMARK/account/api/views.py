from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import EmployeeSerializer
from ..models import *


def apicheck(request):
    return JsonResponse('API  BASE POINT', safe=False)


@api_view(['GET'])
def employee_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        emp = Employee.objects.all().select_related('details')
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class Employeeview(views):
#     model = Employee
#
#     class Meta:
#         pass
