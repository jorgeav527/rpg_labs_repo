from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from orders.models import Order, OrderInfo


@receiver(post_save, sender=Order)
def post_save_order(sender, instance, created, using, update_fields, **kwargs):
    if created:
        OrderInfo.objects.create(order=instance)
    else:
        instance.order_info.save()
