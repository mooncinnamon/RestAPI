from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

# -- User Regi
class UserCreateView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDone(TemplateView):
    template_name = 'registration/register_done.html'