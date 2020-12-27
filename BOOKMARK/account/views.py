# Create your views here.
from django.contrib import messages
from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, View

from .forms import EmployeeForm, EmployeeChangeForm
from .models import *


class LoginView(views.LoginView):
    # authentication_form = EmployeeForm
    template_name = 'account/login.html'

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            # request.session.set_expiry(30)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class EmployeeRegisterView(CreateView):
    model = Employee
    form_class = EmployeeForm

    success_url = reverse_lazy('login')

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #
    #         user = form.save(commit=False)
    #         user.is_active = False # Deactivate account till it is confirmed
    #         user.save()
    #
    #         current_site = get_current_site(request)
    #         subject = 'Activate Your MySite Account'
    #         message = render_to_string('emails/account_activation_email.html', {
    #             'user': user,
    #             'domain': current_site.domain,
    #             'uid': urlsafe_base64_encode(force_bytes(user.pk)),
    #             'token': account_activation_token.make_token(user,form.email),
    #         })
    #         user.email_user(subject, message)
    #
    #         messages.success(request, ('Please Confirm your email to complete registration.'))
    #
    #         return redirect('login')
    #
    #     return render(request, self.template_name, {'form': form})


from django.contrib.auth import login
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token


class ActivateAccount(View):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            # user.profile.email_confirmed = True
            user.save()
            login(request, user)
            messages.success(request, ('Your account have been confirmed.'))
            return redirect('home')
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return redirect('home')


class EmployeeDetailView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Employee
    form_class = EmployeeChangeForm

    success_url = reverse_lazy('hr_page')

    def test_func(self):
        post = self.get_object()
        if self.request.user.get_type == "HR":
            return True
        return False

    def form_valid(self, form):
        # form.instance.author = self.request.user
        # form.instance.title = 'New Title Expected'
        return super().form_valid(form)


class Hr_view(LoginRequiredMixin, ListView):
    template_name = 'account/hr_page.html'
    # queryset = Employee.objects.all()
    model = Employee
    context_object_name = 'employees'
    # paginate_by = 3

    # def get_queryset(self):
    #     return Employee.objects.all().values('username','last_login','empNo','is_active')


class calender_view(LoginRequiredMixin, ListView):
    template_name = 'account/calender.html'
    queryset = Employee.objects.all()[:4]
    model = Employee
    context_object_name = 'employees'
