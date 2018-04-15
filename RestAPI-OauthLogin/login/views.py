from django.shortcuts import render
from rest_framework import generics
from .permissions import IsAuthenticatedOrCreate
from .serializers import SignUpSerializer
from django.contrib.auth import get_user_model

UserModel = get_user_model()


# Create your views here.
class SignUp(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (IsAuthenticatedOrCreate,)
