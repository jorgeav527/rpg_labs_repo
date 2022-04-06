import os
from decimal import Decimal, ROUND_UP

from django.db import models

from orders.models import OrderExecution

IGV = Decimal(os.environ.get("IGV")).quantize(Decimal("0.01"))


class PaidItemExecution(models.Model):
    order_execution = models.ForeignKey(
        OrderExecution,
        on_delete=models.CASCADE,
        verbose_name="paid execution",
        null=True,
        blank=True,
    )
    percentage = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ("pk",)

    def __str__(self):
        return "(%s): %s - %s" % (self.pk, self.order_execution, self.percentage)

    def get_price(self):
        price = Decimal(self.order_execution.get_total_igv_execution() or 0).quantize(
            Decimal("0.01")
        )
        return Decimal(price * self.percentage / 100 or 0).quantize(Decimal("0.01"))
