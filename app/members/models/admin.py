from django.db import models
from django.conf import settings

from members.choices import Professions


class AdminProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='related admin profile')
    created = models.DateTimeField(
        verbose_name='created at', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='updated at', auto_now=True)

    def __str__(self):
        return f'Admin {self.user}'
