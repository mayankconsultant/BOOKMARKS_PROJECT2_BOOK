# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


# class EmployeeType(models.Model):
#     name=models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name


class Employee(AbstractUser):
    class Types(models.TextChoices):
        STANDARD = "STANDARD", "STANDARD"
        LEADER = "LEADER", "LEADER"
        T_MANAGER = 'T_MANAGER', 'T_MANAGER'
        HR = 'HR', 'HR'
        DIRECTOR = 'DIRECTOR', 'DIRECTOR'
        CEO = 'CEO', 'CEO'
        NEWBEE = 'NEWBEE', 'NEWBEE'

    base_type = Types.NEWBEE
    employeetype = models.CharField(_("Type"), max_length=50, choices=Types.choices, default=base_type
                                    )
    Mobile_number = models.CharField(max_length=15)
    Birth_date = models.DateField(null=True, blank=True)
    empNo = models.IntegerField()
    # REQUIRED_FIELDS = ['employeetype']
    objects = CustomUserManager()

    # class Meta:
    #     app_label= 'account'

    def __str__(self):
        return self.get_name

    def get_absolute_url(self):
        return reverse('update_employee', kwargs={'pk': self.pk})

    @property
    def is_hr(self):
        return self.Types.HR == True

    @property
    def get_type(self):
        return self.employeetype

    @property
    def get_name(self):
        return self.first_name + " " + self.last_name

    @property
    def get_gender(self):
        return self.details.gender

    @property
    def get_department(self):
        return self.title.department.name


class StandardEmpManager(models.Manager):
    def get_queryset(self):
        return super(StandardEmpManager, self).get_queryset().filter(employeetype=Employee.Types.STANDARD)


class Standard(Employee):
    objects = StandardEmpManager()

    class Meta:
        proxy = True


class leadermanager(models.Manager):
    def get_queryset(self):
        return super(leadermanager, self).get_queryset().filter(employeetype=Employee.Types.LEADER)


class leader(Employee):
    objects = leadermanager()

    class Meta:
        proxy = True


class HRmanager(models.Manager):
    def get_queryset(self):
        return super(leadermanager, self).get_queryset().filter(employeetype=Employee.Types.HR)


class HR(Employee):
    objects = HRmanager()

    class Meta:
        proxy = True
