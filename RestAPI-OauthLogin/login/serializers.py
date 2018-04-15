from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'password', 'email')


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'password', 'email')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = UserModel(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
