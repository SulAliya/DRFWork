from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from users.models import Payment
from users.serializers import UserSerializer, PaymentSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer


class PaymentListAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('paid_lesson', 'paid_course', 'pay_mothod')
    ordering_fields = ('-date_payment',)
