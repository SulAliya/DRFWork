from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    lessons = SerializerMethodField()

    def get_lessons(self, course):
        return [lesson.title for lesson in Lesson.objects.filter(course=course)]

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    count_lessons = SerializerMethodField()

    def get_count_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ('title', 'description', 'count_lessons')


class LessonDetailSerializer(serializers.ModelSerializer):
    count_lesson_with_same_course = SerializerMethodField()

    # def get_count_lesson_with_same_course(self, lesson):
    #     return Lesson.objects.filter(lesson=lesson.course).count()
    #
    # class Meta:
    #     model = Lesson
    #     fields = ('title', 'course', 'count_course_with_same_lesson')


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
