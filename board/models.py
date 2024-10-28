from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Ad(models.Model):
    TYPE = [
        ('TK', 'Танки'),
        ('HL', 'Хилы'),
        ('DD', 'ДД'),
        ('TD', 'Торговцы'),
        ('GM', 'Гилдмастеры'),
        ('QG', 'Квестгиверы'),
        ('BS', 'Кузнецы'),
        ('TN', 'Кожевники'),
        ('PM', 'Зельевары'),
        ('SM', 'Мастера заклинаний'),
    ]
    title = models.CharField(max_length=255, )
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, )
    category = models.CharField(max_length=16, choices=TYPE, default='TK', )
    creation_time = models.DateTimeField(auto_now_add=True, )
    upload = RichTextUploadingField(blank=True)
    
    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse('ad_detail', args=[str(self.id)])


class UserResponse(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, )
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    text = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True, )
    status = models.BooleanField(default=False, )
    
    def __str__(self):
        return f'{self.user}: {self.text}'
