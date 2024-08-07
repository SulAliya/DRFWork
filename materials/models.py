
from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название', help_text='Укажите название')
    image_preview = models.ImageField(upload_to='materials/photo', verbose_name='Изображение (превью)', **NULLABLE)
    description = models.TextField(verbose_name='Описание', help_text='Опишите курс')

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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
