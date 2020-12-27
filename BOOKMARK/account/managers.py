from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('employeetype', 'HR')
        extra_fields.setdefault('empNo', 99999)
        # base_type = Types.HR
        # extra_fields.setdefault('employeetype','ceo')

        return self.create_user(username, password, **extra_fields)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related('details', 'contacts', 'title')
