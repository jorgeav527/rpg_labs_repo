import os
from decimal import Decimal, ROUND_UP

from django.contrib import admin
from django.db import models
from smart_selects.db_fields import ChainedForeignKey

from orders.models import OrderLiquidation
from tests_labs.models import TestLab, CharacteristicTestLab
from tests_labs.choices import Units
from orders.choices import YesNoUnknown


class OrderItemLiquidation(models.Model):
    order_liquidation = models.ForeignKey(
        OrderLiquidation,
        on_delete=models.CASCADE,
        verbose_name="order liquidation",
        null=True,
        blank=True,
    )
    characteristic_testlab = models.ForeignKey(
        CharacteristicTestLab,
        on_delete=models.SET_NULL,
        verbose_name="characteristic testlab",
        null=True,
        blank=True,
    )
    testlab = ChainedForeignKey(
        TestLab,
        chained_field="characteristic_testlab",
        chained_model_field="characteristic",
        show_all=False,
        auto_choose=False,
        sort=True,
        on_delete=models.SET_NULL,
        verbose_name="testlab",
        null=True,
        blank=True,
    )
    unit = models.CharField(max_length=10, choices=Units.choices, default=Units.NONE)
    quantity = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sampling_by = models.CharField(
        max_length=4,
        choices=YesNoUnknown.choices,
        default=YesNoUnknown.TRUE,
    )

    class Meta:
        ordering = ("pk",)

    def __str__(self):
        return "(%s): %s - %s" % (self.pk, self.order_liquidation, self.testlab)

    def get_partial_igv(self):
        return Decimal(self.price * self.quantity).quantize(
            Decimal("0.01"), rounding=ROUND_UP
        )
