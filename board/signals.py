from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

from .models import *


@receiver(post_save, sender=Ad)
def ad_created(sender, instance, created, **kwargs):
    if created:
        email_list = User.objects.values_list('email', flat=True)
        from_email=settings.DEFAULT_FROM_EMAIL
        subject='Message board'
        message=(
            f'Здравствуйте, добавлено новое объявление на фанатском портале вашей любимой MMORPG!\n'
            f'\n'
            f'Заголовок объявления: "{instance.title}"\n'
            f'Категирия: "{instance.category}"\n'
            f'Просмотр доступер по ссылке: "http://127.0.0.1:8000{instance.get_absolute_url()}".'
        )
        
        for email in email_list:
            send_mail(subject, message, from_email, [email])


@receiver(post_save, sender=UserResponse)
def user_response_created(sender, instance, created, **kwargs):
    if created:
        email=instance.ad.author.email
        from_email=settings.DEFAULT_FROM_EMAIL
        subject='Новый отклик'
        message=(
            f'Здравствуйте, {instance.ad.author.username}!\n'
            f'Вы получили новый отклик на ваше объявление "{instance.ad.title}".\n'
            f'Просмотр доступер по ссылке: "http://127.0.0.1:8000/ads/profile/".'
        )
        
        send_mail(subject, message, from_email, [email])


@receiver(post_save, sender=UserResponse)
def user_response_confirm(instance, **kwargs):
    if instance.status:
        email=instance.user.email
        from_email=settings.DEFAULT_FROM_EMAIL
        subject='Отклик принят'
        message=(
            f'Здравствуйте, {instance.user.username}!\n'
            f'Ваш отклик на объявление "{instance.ad.title}" был принят автором и опубликован.\n'
            f'Просмотр доступер по ссылке: "http://127.0.0.1:8000{instance.get_absolute_url()}".'
        )
        
        send_mail(subject, message, from_email, [email])
