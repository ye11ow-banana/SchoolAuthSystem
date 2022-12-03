from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from accounts.forms import RegistrationForm


class HomeView(TemplateView):
    """
    Start default page.
    E.g. "/".
    """
    template_name = 'accounts/home.html'


class RegistrationView(
    UserPassesTestMixin, SuccessMessageMixin, CreateView
):
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('accounts:login')
    form_class = RegistrationForm
    success_message = 'Your profile was created successfully'
    permission_denied_message = 'You have already logged in!'

    def test_func(self) -> bool:
        return not self.request.user.is_authenticated


home_view = HomeView.as_view()
login_view = LoginView.as_view(
    template_name='accounts/login.html',
    next_page='accounts:home',
    redirect_authenticated_user=True
)
logout_view = LogoutView.as_view(
    next_page='accounts:login'
)
registration_view = RegistrationView.as_view()
