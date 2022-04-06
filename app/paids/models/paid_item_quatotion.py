import os
from decimal import Decimal, ROUND_UP

from django.db import models

from orders.models import OrderQuatotion

IGV = Decimal(os.environ.get("IGV")).quantize(Decimal("0.01"))


class PaidItemQuatotion(models.Model):
    order_quatotion = models.ForeignKey(
        OrderQuatotion,
        on_delete=models.CASCADE,
        verbose_name="paid quatotion",
        null=True,
        blank=True,
    )
    percentage = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ("pk",)

    def __str__(self):
        return "(%s): %s - %s" % (self.pk, self.order_quatotion, self.percentage)

    def get_price(self):
        price = Decimal(self.order_quatotion.get_total_igv_quatotion() or 0).quantize(
            Decimal("0.01")
        )
        return Decimal(price * self.percentage / 100 or 0).quantize(Decimal("0.01"))
