from django.shortcuts import render
from . models import Courses
from . serializers import CoursesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
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
    
    if request.method == 'PUT':
        id=pk
        course =Courses.objects.get(pk=id)
        serialized = CoursesSerializer(course, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response({'msg':'Full data updated Successfully'})
        return Response(serialized.errors)
    
    if request.method == 'PATCH':
        id=pk
        course =Courses.objects.get(pk=id)
        serialized = CoursesSerializer(course, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response({'msg':'Partial data updated Successfully'})
        return Response(serialized.errors)
    
    if request.method == 'DELETE':
        id=pk
        course =Courses.objects.get(pk=id)
        course.delete()
        return Response({'msg':'Data deleted Successfully'})