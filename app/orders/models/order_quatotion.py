import os
from decimal import Decimal, ROUND_UP

from django.contrib import admin
from django.db import models
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey

from companies.models import Company
from projects.models import Project
from members.models import ClientProfile
from orders.choices import TypeService

IGV = Decimal(os.environ.get("IGV")).quantize(Decimal("0.01"))


class OrderQuatotion(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        verbose_name="company_order",
        blank=True,
        null=True,
    )
    project = ChainedForeignKey(
        Project,
        chained_field="company",
        chained_model_field="company",
        show_all=False,
        auto_choose=False,
        sort=True,
        on_delete=models.SET_NULL,
        verbose_name="project_order",
        null=True,
        blank=True,
    )
    client = ChainedForeignKey(
        ClientProfile,
        chained_field="company",
        chained_model_field="company",
        show_all=False,
        auto_choose=False,
        sort=True,
        on_delete=models.SET_NULL,
        verbose_name="client_order",
        null=True,
        blank=True,
    )
    discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )
    quatotion = models.BooleanField(default=True)
    requirement = models.BooleanField(default=True)
    execution = models.BooleanField(default=False)
    liquidation = models.BooleanField(default=False)
    type_service = models.CharField(
        max_length=20,
        choices=TypeService.choices,
        default=TypeService.TEST,
    )
    observation = models.TextField(blank=True, null=True)
    created = models.DateTimeField("created at", auto_now_add=True)
    updated = models.DateTimeField("updated at", auto_now=True)

    class Meta:
        ordering = ("-pk",)
        verbose_name = "order quatotion"
        verbose_name_plural = "orders quatotion"

    def __str__(self):
        return "(%s): %s %s" % (self.pk, self.company, self.created)

    # ORDER QUATOTION
    # @admin.display(description='Parcial')
    def get_sub_total_quatotion(self):
        qs = (
            self.orderitemquatotion_set.filter(order_quatotion=self.pk).values_list(
                "quantity", "price"
            )
            or 0
        )
        s_t = 0 if isinstance(qs, int) else sum(map(lambda q: q[0] * q[1], qs))
        sub_total = Decimal(s_t).quantize(Decimal("0.01"))
        return Decimal(sub_total / IGV or 0).quantize(Decimal("0.01"))

    def get_total_not_igv_quatotion(self):
        return Decimal(self.get_sub_total_quatotion() - self.discount or 0).quantize(
            Decimal("0.01")
        )

    def get_igv_quatotion(self):
        return Decimal(
            self.get_total_not_igv_quatotion() * Decimal(0.18) or 0
        ).quantize(Decimal("0.01"))

    def get_total_igv_quatotion(self):
        return Decimal(
            self.get_total_not_igv_quatotion() + self.get_igv_quatotion() or 0
        ).quantize(Decimal("0.01"))

    # PAID QUATOTION

    def get_total_paid_percentage(self):
        qs = (
            self.paiditemquatotion_set.filter(order_quatotion=self.pk).values_list(
                "percentage"
            )
            or 0
        )
        return Decimal(
            0 if isinstance(qs, int) else sum(map(lambda q: q[0], qs))
        ).quantize(Decimal("0.01"))

    def get_total_paid(self):

        return Decimal(
            self.get_total_igv_quatotion() * self.get_total_paid_percentage() / 100 or 0
        ).quantize(Decimal("0.01"))
