from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .form import UserCreationForm


# Create your views here.
class CreateUserView(CreateView):
    form_class = UserCreationForm


class RegistedSignView(TemplateView):
    template_name = 'rest_login/registed_view.html'