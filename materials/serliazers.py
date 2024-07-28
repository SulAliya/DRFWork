from rest_framework import serializers
from materials.models import Course


class CourseSerializer(serializers.Serializer):

    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.Serializer):

    class Meta:
        model = Course
        fields = '__all__'