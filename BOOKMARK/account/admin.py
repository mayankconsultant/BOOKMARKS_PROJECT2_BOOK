# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import EmployeeForm, EmployeeChangeForm
from .models import Employee


# class EmployeeUserAdmin(admin.ModelAdmin):
#     list_display = ('empNo','employeetype','first_name','date_joined', 'Mobile_number', 'Birth_date','last_login')
#     # list_filter = ('status', 'created', 'publish', 'author')
#     # search_fields = ('title', 'body')
#     # prepopulated_fields = {'slug': ('title',)}
#     # raw_id_fields = ('author',)
#     # date_hierarchy = 'publish'
#     # ordering = ('USERNAME')


class EmployeeUserAdmin(UserAdmin):
    add_form = EmployeeForm
    form = EmployeeChangeForm
    model = Employee
    list_display = (
        'empNo', 'email', 'employeetype', 'first_name', 'date_joined', 'Mobile_number', 'Birth_date', 'last_login')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'empNo'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Employee, EmployeeUserAdmin)

# admin.site.register(Employee.Types)
