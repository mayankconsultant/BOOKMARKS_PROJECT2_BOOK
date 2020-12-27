from account.models import Employee
from django import template
from employees.models import employee_resources

register = template.Library()


@register.simple_tag(name='get_emp_name')
def get_emp_name(emp_id):
    return Employee.objects.get(id=emp_id).get_name


@register.simple_tag(name='chk_emp_resource')
def chk_emp_resource(emp_id, resource_type):
    return employee_resources.objects.filter(employeeid=emp_id, resource_type=resource_type).exists()
