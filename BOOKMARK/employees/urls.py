from django.urls import path

from .views import *

# from django.contrib.auth import views


# from django.contrib.auth.views import PasswordResetView


urlpatterns = [
    # path('allocate_resources/<int:pk>', Employee_resources.as_view(), name='allocate_resources'),
    # path('allocate_resources/<int:pk>', Employee_resourcesCreate.as_view(), name='allocate_resources'),
    path('allocate_resources/<int:pk>', Emp_resource_detail.as_view(), name='allocate_resources'),
]
