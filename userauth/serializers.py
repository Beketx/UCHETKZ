from rest_framework import serializers, exceptions
import django.contrib.auth.password_validation as validators
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('id', 'password', 'email', 'name', 'surname')
        write_only_fields = ('password', )
        read_only_fields = ('id', )

    def create(self, validate_data):
        password = validate_data.pop('password')
        user = models.CustomUser.objects.create(
            **validate_data
        )
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

class ChangePasswordSerializer(serializers.Serializer):
    model = models.CustomUser
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)