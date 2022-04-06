import os
from decimal import Decimal, ROUND_UP

from django.db import models

from orders.models import OrderLiquidation

IGV = Decimal(os.environ.get("IGV")).quantize(Decimal("0.01"))


class PaidItemLiquidation(models.Model):
    order_liquidation = models.ForeignKey(
        OrderLiquidation,
        on_delete=models.CASCADE,
        verbose_name="paid liquidation",
        null=True,
        blank=True,
    )
    percentage = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ("pk",)

    def __str__(self):
        return "(%s): %s - %s" % (self.pk, self.order_liquidation, self.percentage)

    def get_price(self):
        price = Decimal(
            self.order_liquidation.get_total_igv_liquidation() or 0
        ).quantize(Decimal("0.01"))
        return Decimal(price * self.percentage / 100 or 0).quantize(Decimal("0.01"))
