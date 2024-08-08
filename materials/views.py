from rest_framework import viewsets, generics

from materials.models import Course, Lesson
from materials.serliazers import CourseSerializer, LessonSerializer, LessonDetailSerializer, CourseDetailSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CourseDetailSerializer
        return CourseSerializer


class LessonViewSet(viewsets.ModelViewSet):
    # serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         return LessonDetailSerializer
    #     return LessonSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDeleteAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
