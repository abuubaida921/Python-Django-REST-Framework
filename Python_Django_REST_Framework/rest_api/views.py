from django.shortcuts import render
from . models import Courses
from . serializers import CoursesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET', 'POST'])
def course_create(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            #Complex data
            courses=Courses.objects.get(id=pk)
            #Python Dictionary
            serialized = CoursesSerializer(courses)
            return Response(serialized.data)
        
        #Complex data
        courses=Courses.objects.all()
        #Python Dictionary
        serialized = CoursesSerializer(courses,many=True)
        return Response(serialized.data)
    
    if request.method == 'POST':
        serialized = CoursesSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response({'msg':'Data inserted Successfully'})
        return Response(serialized.errors)