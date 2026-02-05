from django.views.generic import TemplateView

from core.mixins import LoginNoRequiredMixin


class HomeView(TemplateView):
    template_name = "index.html"


class LoginView(LoginNoRequiredMixin, TemplateView):
    template_name = "auth/login.html"