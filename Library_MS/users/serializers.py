from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = CustomUsers
       fields = ['username', 'email', 'password']
       extra_kwargs = {'password': {'write_only': True}}


   def create(self, validated_data):
       user = CustomUsers(
           username=validated_data['username'],
           email=validated_data['email']
       )
       user.set_password(validated_data['password'])
       user.save()
       return user

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = "__all__"

class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = "__all__"

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class genderSerializer(serializers.ModelSerializer):
    class Meta:
        model = gender
        fields = "__all__"

class DespositvesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despositves
        fields = "__all__"