from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum

from tests_labs.models import CharacteristicTestLab, TestLab, TestInclude

from decimal import Decimal


@receiver(post_save, sender=TestInclude)
def running_post_save_testinclude(sender, instance, created, raw, update_fields, using, **kwargs):
    # when include add the price
    if created:
        to_test = TestLab.objects.get(pk=instance.to_test_id)
        from_test = TestLab.objects.get(pk=instance.from_test_id)
        to_test.price += Decimal(from_test.price)
        to_test.save()


@receiver(post_delete, sender=TestInclude)
def running_post_delete_testinclude(sender, instance, using, **kwargs):
    # when exclude remove the price
    to_test = TestLab.objects.get(pk=instance.to_test_id)
    from_test = TestLab.objects.get(pk=instance.from_test_id)
    to_test.price -= Decimal(from_test.price)
    to_test.save()
