from django.db.models.signals import post_save, pre_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver

from members.models import AdminProfile, ClientProfile
from members.choices import Roles

USER = get_user_model()


@receiver(post_save, sender=USER)
def post_save_user_roles(sender, instance, created, using, update_fields, **kwargs):
    if instance.role == Roles.CLIENT:
        if created:
            ClientProfile.objects.create(user=instance)
        else:
            instance.clientprofile.save()
    elif instance.role == Roles.ADMIN:
        if created:
            AdminProfile.objects.create(user=instance)
        else:
            instance.adminprofile.save()
