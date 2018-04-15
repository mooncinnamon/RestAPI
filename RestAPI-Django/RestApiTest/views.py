from django.shortcuts import render
from rest_framework import viewsets
from RestApiTest.serializers import TestSerializer
from RestApiTest.models import RestTest

# Create your views here.
class RestTestViewSet(viewsets.ModelViewSet):
    queryset = RestTest.objects.all()
    serializer_class = TestSerializer