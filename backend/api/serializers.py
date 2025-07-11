from django.contrib.auth.models import User
from rest_framework import serializers
from.models import Notes, SudokuModel
import json
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs = {"password":{"write_only":True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class Noteserializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ["id","Title","Content","created_at","author"]
        extra_kwargs = {"author":{"read_only":True}}


class SudokuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudokuModel
        fields = ["id","Boards","author","created_at"]
        read_only_fields = ["author", "created_at"]
    