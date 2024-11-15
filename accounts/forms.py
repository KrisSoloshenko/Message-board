from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.conf import settings
from string import hexdigits
from .models import Code

import random


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.is_active = False
        user.save()
        random_code = ''.join(random.sample(hexdigits, k=6))
        Code.objects.create(code=random_code, user=user)
        send_mail(
            subject=f'Код активации',
            message=f'Код для активации аккаунта {random_code}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email]
        )        
        return user
    