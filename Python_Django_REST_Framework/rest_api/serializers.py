from rest_framework import serializers
from . models import Courses

class CoursesSerializer(serializers.Serializer):
    teacher_name=serializers.CharField(max_length=25)
    course_name=serializers.CharField(max_length=20)
    course_duration = serializers.IntegerField()
    seat = serializers.IntegerField()

    def create(self, validated_data):
        return Courses.objects.create(**validated_data)