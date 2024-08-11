from django.shortcuts import render
from . models import Courses
from . serializers import CoursesSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser

# Create your views here.
#QuerySet
def courses_info(request):
    #Complex data
    courses=Courses.objects.all()
    #Python Dictionary
    serialized = CoursesSerializer(courses,many=True)
    #Render to json
    json_data=JSONRenderer().render(serialized.data)
    #Send to user for view
    return HttpResponse(json_data, content_type='application/json')

#Model Object
def courses_instance(request, pk):
    #Complex data
    courses=Courses.objects.get(id=pk)
    #Python Dictionary
    serialized = CoursesSerializer(courses)
    #Render to json
    json_data=JSONRenderer().render(serialized.data)
    #Send to user for view
    return HttpResponse(json_data, content_type='application/json')

#Create new data
@csrf_exempt
def course_create(request):
    if request.method == "POST":
        print('===============================')
        print(request.body)
        print('===============================')
        json_data=request.body
        #json to stream
        stream=io.BytesIO(json_data)
        #stream to python
        pythonData= JSONParser().parse(stream)
        #python to complex
        serialized = CoursesSerializer(data=pythonData)
        if serialized.is_valid():
            serialized.save()
            res = {'msg':'Data inserted successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serialized.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method == "PUT":
        json_data=request.body
        #json to stream
        stream=io.BytesIO(json_data)
        #stream to python
        pythonData= JSONParser().parse(stream)
        id=pythonData.get('id')
        courseID=Courses.objects.get(id=id)
        #python to complex
        serialized = CoursesSerializer(courseID,data=pythonData,partial=True)
        if serialized.is_valid():
            serialized.save()
            res = {'msg':'Data updated successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serialized.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method == "DELETE":
        json_data=request.body
        #json to stream
        stream=io.BytesIO(json_data)
        #stream to python
        pythonData= JSONParser().parse(stream)
        id=pythonData.get('id')
        courseID=Courses.objects.get(id=id)
        courseID.delete()
        res = {'msg':'Data deleted successfully'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')