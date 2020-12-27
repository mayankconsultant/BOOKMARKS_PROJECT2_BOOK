from django.conf import settings
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

user = settings.AUTH_USER_MODEL


class employeedetails(models.Model):
    class Gender(models.TextChoices):
        MALE = ("MALE", "MALE")
        FEMALE = ("FEMALE", "FEMALE")

    employeeid = models.OneToOneField(user, on_delete=models.DO_NOTHING, verbose_name="NameEmployee",
                                      related_name='details')
    gender = models.CharField(max_length=10, choices=Gender.choices, blank=True, null=True)
    marital_status = models.CharField(max_length=10, null=True, blank=True, default="Single")
    nationality = models.CharField(max_length=20, null=True, blank=True, default="South Sudani")
    nssf_no = models.CharField(max_length=20, null=True, blank=True)
    telephone_no = models.CharField(max_length=20, null=True, blank=True)


class ResourceManager(models.Manager):
    def active(self, **kwargs):
        return self.filter(deassigned_date__isnull=True, **kwargs)

    def deactive(self, **kwargs):
        return self.filter(deassigned_date__isnull=False, **kwargs)


class employee_resources(models.Model):
    class Resource_type(models.TextChoices):
        LAPTOP = ("LAPTOP", "LAPTOP")
        WORKSTATION = ("WORKSTATION", "WORKSTATION")
        MOBILE = ("MOBILE", "MOBILE")
        DATACARD = ("DATACARD", "DATACARD")

    employeeid = models.ForeignKey(user, on_delete=models.DO_NOTHING, related_name='resources')
    resource_type = models.CharField(max_length=25, choices=Resource_type.choices, blank=True, null=True)
    resource_id = models.CharField(max_length=40, blank=True, null=True)
    assigned_date = models.DateTimeField(blank=True, null=True)
    deassigned_date = models.DateTimeField(blank=True, null=True)
    deassigned_comments = models.TextField(blank=True, null=True)

    objects = ResourceManager()


class employee_contacts(models.Model):
    employeeid = models.OneToOneField(user, on_delete=models.DO_NOTHING, related_name='contacts')
    address1 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    home_number = models.CharField(max_length=20)


class Status(models.TextChoices):
    ACTIVE = ("ACTIVE", "ACTIVE")
    STOPPED = ("STOPPED", "STOPPED")
    OUTSOURCED = ("OUTSOURCED", "OUTSOURCED")
    SUSPENDED = ("SUSPENDED", "SUSPENDED")


class department(models.Model):
    name = models.CharField(max_length=45)
    status = models.CharField(max_length=15, choices=Status.choices, blank=True, null=True, default="ACTIVE")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class team(models.Model):
    name = models.CharField(max_length=45)
    status = models.CharField(max_length=15, choices=Status.choices, blank=True, null=True, default="ACTIVE")
    department = models.ForeignKey(department, on_delete=models.DO_NOTHING, related_name="under")
    t_level = models.PositiveSmallIntegerField(default=1)
    t_parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL, related_name='parent')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class position(models.Model):
    name = models.CharField(max_length=45, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class employee_position(models.Model):
    employee = models.OneToOneField(user, on_delete=models.DO_NOTHING, related_name='title')
    position = models.ForeignKey(position, on_delete=models.DO_NOTHING, related_name='position')
    position_start_date = models.DateField(auto_now=True)
    position_end_date = models.DateField(blank=True, null=True)
    reason = models.CharField(max_length=50, blank=True, null=True)
    department = models.ForeignKey(department, on_delete=models.DO_NOTHING, related_name='department', default=1)
    team = models.ForeignKey(team, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='team')

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('department')
        print('Query-->' + str(qs))
        return qs


class teams(MPTTModel):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(department, on_delete=models.DO_NOTHING)
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='children')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
