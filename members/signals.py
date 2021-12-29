from django.db.models.signals import post_save, pre_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver

from .models import AdminProfile
from .choices import Roles

USER = get_user_model()


@receiver(post_save, sender=USER)
def create_or_update_customuser_profile(sender, instance, created, **kwargs):
    if instance.role == Roles.ADMIN:
        if created:
            AdminProfile.objects.create(user=instance)
        else:
            instance.adminprofile.save()
