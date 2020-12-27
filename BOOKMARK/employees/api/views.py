from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from employees.models import employee_resources, teams, department
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import EmpResSerializer, teamsSer, departmentSer


def apicheck(request):
    return JsonResponse('API  BASE POINT', safe=False)


class Teams_CRU(generics.ListAPIView):
    serializer_class = teamsSer
    queryset = teams.objects.all()


class department_CRU(generics.ListAPIView):
    serializer_class = departmentSer
    queryset = department.objects.all()


class CRU(generics.ListCreateAPIView):
    # queryset = employee_resources.objects.active()
    serializer_class = EmpResSerializer
    lookup_field = ['employeeid']

    def get_queryset(self):
        print("reading get_querset")
        print(self.queryset)
        return self.queryset

    def list(self, request, pk):
        queryset = employee_resources.objects.active(employeeid=pk)
        serializer = EmpResSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        # print(self)
        # print(serializer['employeeid'])
        serializer.save()
        return Response(serializer.data)


class RUD(generics.RetrieveUpdateAPIView):
    lookup_field = ['pk']
    queryset = employee_resources.objects.all()
    serializer_class = EmpResSerializer
    url_kwarg = 'id'

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            id=self.kwargs.get('id')
        )
    #
    # def patch(self,serializer):
    #     print("Patch")
    #     print(serializer)
    #     serializer.save()
    #     return Response(serializer.data)


@api_view(['GET'])
def employee_resource(request, employeeid):
    """
    List all code snippets, or create a new snippet.
    """
    try:
        emp = employee_resources.objects.filter(employeeid=employeeid)
    except:
        return Response(status=404)

    if request.method == 'GET':
        # print(emp.assigned_date)
        serializer = EmpResSerializer(emp, many=True)
        # print(serializer.data)
        return Response(serializer.data)


@api_view(["POST"])
@csrf_exempt
def add_resource(request, employeeid):
    # request["employeeid"]=employeeid
    serializer = EmpResSerializer(data=request.data)

    if serializer.is_valid():
        print("Success")
        # print(serializer)
        serializer.save()
    else:
        print("ERROR")
        print(serializer.errors)
    return Response(serializer.data)


@api_view(["PUT"])
@csrf_exempt
def update_resource(request, id):
    # request["employeeid"]=employeeid
    payload = json.loads(request.body)
    emp = employee_resources.objects.filter(id=id)

    try:
        emp.update(**payload)

        res = employee_resources.objects.filter(id=id)
        serializer = EmpResSerializer(res)
        return JsonResponse({'resource': serializer.data}, safe=False, status=status.HTTP_200_OK)

    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # serializer = EmpResSerializer(emp)
    #
    # if serializer.is_valid():
    #     print("Success")
    #     # print(serializer)
    #     serializer.save()
    #     return Response(serializer.data)
    # else:
    #     print("ERROR" )
    #     print(serializer.errors)
    # return Response(serializer.errors)

# @api_view(["POST"])
# @csrf_exempt
# def add_resource(request):
#     # print(request.data)
#
#     payload = json.loads( request.data)
#     # user = request.user
#     try:
#         # emp = Employee.objects.get(id=employeeid)
#         empre = employee_resources.objects.create(
#             resource_type=payload.get("resource_type"),
#             resource_id=payload.get("resource_id"),
#             assigned_date=payload.get("assigned_date"),
#             employeeid=employeeid
#         )
#         serializer = EmpResSerializer(empre)
#         print(serializer)
#         return JsonResponse( serializer.data, safe=False, status=status.HTTP_201_CREATED)
#     except ObjectDoesNotExist as e:
#         return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
#     except Exception:
#         return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#

# class Employeeview(views):
#     model = Employee
#
#     class Meta:
#         pass
