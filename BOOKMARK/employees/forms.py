from django.conf import settings
from django.forms import ModelForm

from .models import employee_resources, employee_position

# from django.forms.models import inlineformset_factory

# from account.models import Employee

user = settings.AUTH_USER_MODEL


class employeeresourceForm(ModelForm):
    readonly = ('employeeid',)

    class Meta:
        model = employee_resources
        fields = '__all__'
        labels = {
            "employeeid": "Employee Name"
        }

    # employeeInlineFormset = inlineformset_factory(Employee, employee_resources, form=employeeresourceForm, extra=4,
    #                                                   can_delete=True)

    def __init__(self, *arg, **kwrg):
        super(employeeresourceForm, self).__init__(*arg, **kwrg)
        print(" Kwargs1 ")
        print(self)
        for x in self.readonly:
            self.fields[x].widget.attrs['disabled'] = 'disabled'

    def clean(self):
        data = super(employeeresourceForm, self).clean()
        for x in self.readonly:
            data[x] = getattr(self.instance, x)
        return data


class employee_positionForm(ModelForm):
    readonly = ('employeeid',)

    class Meta:
        model = employee_position
        fields = '__all__'
        labels = {
            "employeeid": "Employee Name"
        }

    # employeeInlineFormset = inlineformset_factory(Employee, employee_resources, form=employeeresourceForm, extra=4,
    #                                                   can_delete=True)

    def __init__(self, *arg, **kwrg):
        super(employee_positionForm, self).__init__(*arg, **kwrg)
        print(" Kwargs1 ")
        print(self)
        for x in self.readonly:
            self.fields[x].widget.attrs['disabled'] = 'disabled'

    def clean(self):
        data = super(employee_positionForm, self).clean()
        for x in self.readonly:
            data[x] = getattr(self.instance, x)
        return data
