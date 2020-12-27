from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Employee


class EmployeeForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta(UserCreationForm):
        model = Employee
        fields = ('username', 'email', 'password1',
                  'password2', 'empNo')

    def __init__(self, *args, **kwargs):
        # kwargs['request'].delete

        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['empNo'].initial = 99999


class EmployeeChangeForm(UserChangeForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')

    class Meta:
        model = Employee
        fields = ('username', 'empNo', 'employeetype', 'email', 'first_name', 'last_name')
