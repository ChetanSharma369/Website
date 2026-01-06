from rest_framework import serializers
from . models import Person, Colors, PersonDetail

class ColorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = ['color_name']

class login(serializers.Serializer):
    username = serializers.EmailField()
    password = serializers.CharField(max_length=100)

class PersonSerializer(serializers.ModelSerializer):
    colors = ColorsSerializer()
    color_info = serializers.SerializerMethodField()

    def get_color_info(self, obj):
        color_obj = Colors.objects.get(id=obj.colors.id)
        return { "id": color_obj.color_name , "code": "###001"}


    class Meta:
        model = Person
        fields = '__all__' 
        
    def validate(self,data):
        if any(char in '!@#$%^&*()' for char in data.get('name', '')):
            raise serializers.ValidationError("Name contains invalid characters")
        if data.get('age') < 5:
            raise serializers.ValidationError("Age is smaller")

class PersonDetailSerializer(serializers.ModelSerializer):
    person = PersonSerializer()
    class Meta:
        model = PersonDetail
        fields = '__all__'