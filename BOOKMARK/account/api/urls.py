from django.urls import path

from .views import Employeeview

urlpatterns = [
    path('hr', Employeeview.as_view(), name='api-employee'),
]
