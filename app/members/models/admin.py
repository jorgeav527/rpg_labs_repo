from django.db import models
from django.conf import settings

from members.choices import Charges


class AdminProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="related admin profile",
    )
    charge = models.CharField(
        max_length=10,
        choices=Charges.choices,
        default=Charges.NONE,
    )
    created = models.DateTimeField("created at", auto_now_add=True)
    updated = models.DateTimeField("updated at", auto_now=True)

    def __str__(self):
        return f"Admin {self.user}"
