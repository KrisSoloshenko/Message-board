from django.db import models
from django.contrib.auth.models import User


class Code(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null=True, blank=True)
    code = models.CharField(max_length=10, default=0)
