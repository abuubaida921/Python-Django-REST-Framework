from django.shortcuts import render
from . models import Courses
from . serializers import CoursesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class course_create(APIView):
    def get(self,request, pk=None,format=None):
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
    
    def post(self,request,format=None):
        serialized = CoursesSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response({'msg':'Data inserted Successfully'})
        return Response(serialized.errors)
    
    def put(self,request, pk,format=None):
        id=pk
        course =Courses.objects.get(pk=id)
        serialized = CoursesSerializer(course, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response({'msg':'Full data updated Successfully'})
        return Response(serialized.errors)
    
    def patch(self,request, pk,format=None):
        id=pk
        course =Courses.objects.get(pk=id)
        serialized = CoursesSerializer(course, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response({'msg':'Partial data updated Successfully'})
        return Response(serialized.errors)
    
    def delete(self,request, pk,format=None):
        id=pk
        course =Courses.objects.get(pk=id)
        course.delete()
        return Response({'msg':'Data deleted Successfully'})