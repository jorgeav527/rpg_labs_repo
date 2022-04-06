from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

from orders.models import (
    OrderQuatotion,
    OrderExecution,
    OrderLiquidation,
    OrderInfo,
    OrderItemQuatotion,
    OrderItemExecution,
    OrderItemLiquidation,
)
from paids.models import PaidItemQuatotion, PaidItemExecution, PaidItemLiquidation


@receiver(post_save, sender=OrderQuatotion)
def post_save_orderinfo(sender, instance, created, using, update_fields, **kwargs):
    if created:
        OrderInfo.objects.create(order_quotation=instance)
    else:
        instance.orderinfo.save()


@receiver(post_save, sender=OrderQuatotion)
def post_save_orderexecution_execution(
    sender, instance, created, using, update_fields, **kwargs
):
    if instance.execution:
        OrderExecution.objects.get_or_create(
            order_quatotion=instance, discount=instance.discount
        )
    if instance.execution == False:
        try:
            OrderExecution.objects.get(order_quatotion=instance).delete()
        except ObjectDoesNotExist:
            pass


@receiver(post_save, sender=OrderQuatotion)
def post_save_orderexecution_liquidation(
    sender, instance, created, using, update_fields, **kwargs
):
    if instance.liquidation:
        OrderLiquidation.objects.get_or_create(
            order_execution=instance.orderexecution,
            discount=instance.orderexecution.discount,
        )
    if instance.liquidation == False:
        try:
            OrderLiquidation.objects.get(
                order_execution=instance.orderexecution.orderliquidation.pk
            ).delete()
        except ObjectDoesNotExist:
            pass


@receiver(post_save, sender=OrderExecution)
def post_save_orderitemexecution(
    sender, instance, created, using, update_fields, **kwargs
):
    if created:
        qs_quatotion = OrderItemQuatotion.objects.filter(
            order_quatotion__id=instance.order_quatotion_id
        )
        qs_paid_quatotion = PaidItemQuatotion.objects.filter(
            order_quatotion__id=instance.order_quatotion_id
        )
        for item in qs_quatotion:
            OrderItemExecution.objects.create(
                order_execution=instance,
                characteristic_testlab=item.characteristic_testlab,
                testlab=item.testlab,
                unit=item.unit,
                quantity=item.quantity,
                price=item.price,
                sampling_by=item.sampling_by,
            )
        for item in qs_paid_quatotion:
            PaidItemExecution.objects.create(
                order_execution=instance,
                percentage=item.percentage,
            )


@receiver(post_save, sender=OrderLiquidation)
def post_save_orderitemliquidation(
    sender, instance, created, using, update_fields, **kwargs
):
    if created:
        qs_execution = OrderItemExecution.objects.filter(
            order_execution__id=instance.order_execution_id
        )
        qs_paid_execution = PaidItemExecution.objects.filter(
            order_execution__id=instance.order_execution_id
        )
        for item in qs_execution:
            OrderItemLiquidation.objects.create(
                order_liquidation=instance,
                characteristic_testlab=item.characteristic_testlab,
                testlab=item.testlab,
                unit=item.unit,
                quantity=item.quantity,
                price=item.price,
                sampling_by=item.sampling_by,
            )
        for item in qs_paid_execution:
            PaidItemLiquidation.objects.create(
                order_liquidation=instance,
                percentage=item.percentage,
            )
