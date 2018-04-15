from django.views.generic.base import TemplateView

from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from rest_framework import viewsets

from login.serializers import UserSerializer

UserModel = get_user_model()


class IndexView(TemplateView):
    template_name = 'index.html'


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class UserCreateDone(TemplateView):
    template_name = 'registration/register_done.html'


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
