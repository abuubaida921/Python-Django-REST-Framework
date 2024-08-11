from django.shortcuts import render
from . models import Courses
from . serializers import CoursesSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

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