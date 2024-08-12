from rest_framework import serializers
from . models import Courses

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model =Courses
        fields=['id','teacher_name','course_name','course_duration','seat']