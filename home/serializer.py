from rest_framework import serializers
from . models import Person, Colors, PersonDetail, Students
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.save()
        return user

    def validate(self,request):
        username = request.get('username')
        email = request.get('email')
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('Username already exists')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email already exists')
        return request


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

    
class ColorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = ['color_name']

class login(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__' 
        
    def validate(self,data):
        name = data.get('name')
        if any(char in '!@#$%^&*()' for char in name):
            raise serializers.ValidationError("Name contains invalid characters")
        age = data.get('age')
        if age < 5:
            raise serializers.ValidationError("Age is smaller")
        return data

class PersonDetailSerializer(serializers.ModelSerializer):
    person = PersonSerializer()
    class Meta:
        model = PersonDetail
        fields = '__all__'