from django.contrib import admin

# Register your models here.
from materials.models import Lesson, Course

admin.site.register(Lesson)
admin.site.register(Course)