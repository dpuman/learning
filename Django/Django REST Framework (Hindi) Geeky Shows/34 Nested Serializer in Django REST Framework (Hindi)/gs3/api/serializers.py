from dataclasses import field
from rest_framework import serializers
from .models import Singer, Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class SingerSerializer(serializers.ModelSerializer):
    sungby = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'sungby']
