from django.contrib import admin
from . models import Courses

# Register your models here.
@admin.register(Courses)

#display style
class CoursesAdmin(admin.ModelAdmin):
    list_display=['id','teacher_name','course_name','course_duration','seat']