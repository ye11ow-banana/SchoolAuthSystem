from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """
    Start default page.
    E.g. "/".
    """
    template_name = 'accounts/home.html'


home_view = HomeView.as_view()
login_view = LoginView.as_view(
    template_name='accounts/login.html',
    next_page='accounts:home'
)
logout_view = LogoutView.as_view(
    template_name='accounts/logout.html',
    next_page='accounts:login'
)
