from django.views.generic.base import TemplateView

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'index.html'


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class UserCreateDone(TemplateView):
    template_name = 'registration/register_done.html'
