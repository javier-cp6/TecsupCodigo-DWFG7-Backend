from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User

class RegisterSerializer(serializers.ModelSerializer):

  # optional
  # email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
  passwordchecker = serializers.CharField(write_only=True, required=True)

  class Meta:
    model = User
    # fields = '__all__'
    fields = ('name', 'lastname','email', 'password', 'passwordchecker')

  def validate(self, attrs):
    if attrs['password'] != attrs['passwordchecker']:
      raise serializers.ValidationError("Passwords didn't match")
    return attrs
  
  def create(self, validated_data):
    user = User.objects.create(
      name = validated_data['name'],
      lastname = validated_data['lastname'],
      email = validated_data['email'],
      password = validated_data['password'],
    )
    user.set_password(validated_data['password'])
    user.save()
    return user