from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from materials.models import Course, Lesson, Subscription
from materials.validators import YoutubeLinkValidator


class LessonSerializer(serializers.ModelSerializer):
    validators = [YoutubeLinkValidator(field='video')]
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons = SerializerMethodField(read_only=True)

    def get_lessons(self, course):
        return [lesson.title for lesson in Lesson.objects.filter(course=course)]

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()

    def get_count_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_subscription(self, course):
        user = self.context.get('request').user
        course = self.context.get('view').kwargs.get('pk')
        subscription = Subscription.objects.filter(user=user, course=course)
        if subscription.exists():
            return True
        else:
            return False

    class Meta:
        model = Course
        fields = ('title', 'description', 'count_lessons')


class LessonDetailSerializer(serializers.ModelSerializer):
    count_lesson_with_same_course = SerializerMethodField()


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
