from account.models import Employee
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, TemplateView

from .models import employee_resources, employee_position


# Create your views here.


class Emp_Position(LoginRequiredMixin, CreateView):
    model = employee_position
    context_object_name = 'positions'
    queryset = employee_position.objects.all()
    template_name = 'employees/emp_position.html'

    def get_queryset(self):
        id = get_object_or_404(Employee, id=self.kwargs['pk'])
        return self.queryset.filter(employeeid=id)


class Emp_resource_detail(TemplateView):
    model = employee_resources
    template_name = 'employees/emp_resources.html'
    context_object_name = 'resources'

    # queryset = employee_resources.objects.all()

    # def get_queryset(self):
    #     id = get_object_or_404(Employee, id=self.kwargs['pk'])
    #     # id = self.kwargs['pk']
    #     qs = self.queryset.filter(employee = id).prefetch_related(Prefetch('employee',queryset=Employee.objects.filter(id = id )))
    #     print('QUErY SET ')
    #     print(qs.employee.getname)
    #     return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["employeeid"] = self.kwargs['pk']
        # context['name']=employee_position.objects.filter(employee=self.kwargs['pk']).prefetch_related(Prefetch('employee',queryset=Employee.objects.get(id=self.kwargs['pk'] )))
        # context["form"]=employeeresourceForm
        print(context)
        return context

# class Employee_resourcesCreate(CreateView):
#     model = employee_resources
#     form_class = employeeInlineFormset
#     success_url = reverse_lazy('hr_page')
#
#     # def get(self, request, *args, **kwargs):
#     #     print(kwargs)
#     #     self['empid']=kwargs['pk']
#     #     return super().get(self, request, *args, **kwargs)
#
#     # def get_object(self, querset=None):
#     #     # get the existing object or created a new one
#     #     employee = Employee.objects.get(pk=self.kwargs['pk'])
#     #     # obj, created = employee_resources.objects.update_or_create(employeeid=employee.id)
#     #     obj, created = employee_resources.objects.get_or_create(employeeid=employee)
#     #     print(obj)
#     #     return obj
#     #
#     # def get_context_data(self, **kwargs):
#     #     print(self)
#     #     context = super(Employee_resourcesCreate, self).get_context_data(**kwargs)
#     #     # empobj = Employee.objects.get(pk =obj)
#     #     # obj = employee_resources.objects.get_or_create(employeeid = empobj)
#     #     # context['all_forms'] = employeeInlineFormset(instance=obj)
#     #     return context
#     #
#     # def post(self, request, *args, **kwargs):
#     #     formset = employeeInlineFormset(request.POST)
#     #     if formset.is_valid() :
#     #         return self.form_valid(formset)
#
#     def form_valid(self, formset):
#
#         formset.instance.employeeid= Employee.objects.get(pk=self.kwargs.get('pk'))
#         return super(Employee_resourcesCreate, self).form_valid()
