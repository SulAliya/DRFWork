
from django.db import models

from config import settings
from config.settings import AUTH_USER_MODEL


NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название', help_text='Укажите название')
    image_preview = models.ImageField(upload_to='materials/photo', verbose_name='Изображение (превью)', **NULLABLE)
    description = models.TextField(verbose_name='Описание', help_text='Опишите курс')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название', help_text='Укажите название')
    image_preview = models.ImageField(upload_to='materials/photo', verbose_name='Изображение (превью)', **NULLABLE)
    description = models.TextField(verbose_name='Описание', help_text='Опишите урок')
    link = models.URLField(max_length=300, verbose_name='Ссылка на видео', help_text='Укажите ссылку на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', related_name='lessons', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Subscription(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Пользователь")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="Курс")
    def __str__(self):
        return f"{self.user} - {self.course}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"