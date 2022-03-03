from django.db import models
from django.conf import settings

from companies.models import Company
from members.models import User

from members.choices import Professions


class ClientProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="related client profile"
    )
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=True, verbose_name="the related company"
    )
    created = models.DateTimeField(verbose_name="created at", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="updated at", auto_now=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"Client {self.user}"
