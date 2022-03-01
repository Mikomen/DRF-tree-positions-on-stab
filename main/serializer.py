from rest_framework import serializers
from .models import *

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name']

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['id', 'name']

class ChildEmployersSerializer(serializers.ModelSerializer):

    position = PositionSerializer(many=True)
    level = LevelSerializer(read_only=True)

    class Meta:
        model = Employers
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'level', 'position',  'user']

class FullEmployersSerializer(serializers.ModelSerializer):

    position = PositionSerializer(many=True)
    level = LevelSerializer(read_only=True)
    user = ChildEmployersSerializer(many=True)

    class Meta:
        model = Employers
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'level', 'position', 'user']

class EmployersSerializer(serializers.ModelSerializer):

    position = PositionSerializer(many=True)
    level = LevelSerializer(read_only=True)

    class Meta:
        model = Employers
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'level', 'position']

