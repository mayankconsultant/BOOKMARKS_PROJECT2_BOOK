from django.contrib.auth import views as auth_views
from django.urls import path, include
from employees.api.views import *

from .api.views import *
from .views import *

# from django.contrib.auth import views

# from django.contrib.auth.views import PasswordResetView

urlpatterns = [
    path('', include('employees.urls')),
    path('api/', apicheck, name='api-check'),
    path('api/employees', employee_list, name='api-employees'),
    path('api/emp_resource/<int:employeeid>', employee_resource, name='api-employees-resource'),
    path('api/add_resource/<int:employeeid>', add_resource, name='api-employees-resource-add'),
    path('api/update_resource/<int:id>/', update_resource, name='api-employees-resource-update'),
    path('login/', LoginView.as_view(), name='login'),
    path('api/cru/<int:pk>', CRU.as_view(), name='api-cru'),
    path('ajax/teams', Teams_CRU.as_view(), name='ajax-team'),
    path('ajax/department', department_CRU.as_view(), name='ajax-department'),
    path('api/rud/<int:id>', RUD.as_view(), name='api-rud'),
    path('hr/', Hr_view.as_view(), name='hr_page'),
    path('calender/', calender_view.as_view(), name='calender_page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('update/<int:pk>', EmployeeDetailView.as_view(), name='update_employee'),
    path('register/', EmployeeRegisterView.as_view(), name='create_employee'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('json/', auth_views.TemplateView.as_view(template_name='account/json.html'), name='json'),
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'),
        name='password_reset'
    ),
    path(
        'password_reset_done/',
        auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    path(
        'password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
        name='password_reset_complete'
    ),
    path(
        'password-change/',
        auth_views.PasswordChangeView.as_view(template_name='account/password_change.html'),
        name='password_change'
    ),
    path(
        'password-change-Done/',
        auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'),
        name='password_change_done'
    ),

]
