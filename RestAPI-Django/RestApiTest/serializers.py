from rest_framework import serializers
from RestApiTest.models import RestTest

class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RestTest
        fields = '__all__'