import os
from decimal import Decimal, ROUND_UP

from django.contrib import admin
from django.db import models
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey

from orders.models import OrderQuatotion

IGV = Decimal(os.environ.get("IGV")).quantize(Decimal("0.01"))


class OrderExecution(models.Model):
    order_quatotion = models.OneToOneField(OrderQuatotion, on_delete=models.CASCADE)
    discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )
    observation = models.TextField(blank=True, null=True)
    created = models.DateTimeField("created at", auto_now_add=True)
    updated = models.DateTimeField("updated at", auto_now=True)

    class Meta:
        ordering = ("-pk",)
        verbose_name = "order execution"
        verbose_name_plural = "orders execution"

    def __str__(self):
        return "(%s): %s" % (self.pk, self.discount)

    # ORDER EXECUTION
    def get_sub_total_execution(self):
        qs = (
            self.orderitemexecution_set.filter(order_execution=self.pk).values_list(
                "quantity", "price"
            )
            or 0
        )
        s_t = 0 if isinstance(qs, int) else sum(map(lambda q: q[0] * q[1], qs))
        sub_total = Decimal(s_t).quantize(Decimal("0.01"))
        return Decimal(sub_total / IGV or 0).quantize(Decimal("0.01"))

    def get_total_not_igv_execution(self):
        return Decimal(self.get_sub_total_execution() - self.discount or 0).quantize(
            Decimal("0.01")
        )

    def get_igv_execution(self):
        return Decimal(
            self.get_total_not_igv_execution() * Decimal(0.18) or 0
        ).quantize(Decimal("0.01"))

    def get_total_igv_execution(self):
        return Decimal(
            self.get_total_not_igv_execution() + self.get_igv_execution() or 0
        ).quantize(Decimal("0.01"))

    def get_diference_quatotion_execution(self):
        return Decimal(
            self.get_total_igv_execution()
            - self.order_quatotion.get_total_igv_quatotion()
            or 0
        ).quantize(Decimal("0.01"))

    # PAID EXECUTION

    def get_total_paid_percentage(self):
        qs = (
            self.paiditemexecution_set.filter(order_execution=self.pk).values_list(
                "percentage"
            )
            or 0
        )
        return Decimal(
            0 if isinstance(qs, int) else sum(map(lambda q: q[0], qs))
        ).quantize(Decimal("0.01"))

    def get_total_paid(self):
        return Decimal(
            self.get_total_igv_execution() * self.get_total_paid_percentage() / 100 or 0
        ).quantize(Decimal("0.01"))

    def get_debt_paid(self):
        return Decimal(
            self.get_total_igv_execution() - self.get_total_paid() or 0
        ).quantize(Decimal("0.01"))
