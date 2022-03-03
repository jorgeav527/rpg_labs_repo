import os
from decimal import Decimal, ROUND_UP
from datetime import datetime, date

from django.contrib import admin
from django.db import models
from django.forms import inlineformset_factory

from tests_labs.models import TestLab, CharacteristicTestLab
from companies.models import Company
from projects.models import Project
from members.models import ClientProfile, AdminProfile
from orders.choices import TypeService, TypeResponsible, TypeLegalRequirements

IGV = Decimal(os.environ.get("IGV")).quantize(Decimal("0.01"))


class Order(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        verbose_name="company_order",
        null=True,
        blank=True,
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        verbose_name="project_order",
        null=True,
        blank=True,
    )
    client = models.ForeignKey(
        ClientProfile,
        on_delete=models.SET_NULL,
        verbose_name="client_order",
        null=True,
        blank=True,
    )
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cost_quatotion = models.BooleanField(default=True)
    requirement = models.BooleanField(default=False)
    execution_order = models.BooleanField(default=False)
    liquidation = models.BooleanField(default=False)
    type_service = models.CharField(
        max_length=20, choices=TypeService.choices, default=TypeService.TEST
    )
    created = models.DateTimeField(verbose_name="created at", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="updated at", auto_now=True)

    class Meta:
        ordering = ("-pk",)
        verbose_name = "order"
        verbose_name_plural = "orders"

    def __str__(self):
        return "(%s): %s" % (self.pk, self.discount)

    # @admin.display(description='Parcial')
    def get_sub_total(self):
        qs = (
            self.order_items.filter(order=self.pk).values_list("quantity", "price") or 0
        )
        s_t = 0 if isinstance(qs, int) else sum(map(lambda q: q[0] * q[1], qs))
        sub_total = Decimal(s_t).quantize(Decimal("0.01"))
        return Decimal(sub_total / IGV or 0).quantize(Decimal("0.01"))

    def get_total_not_igv(self):
        return Decimal(self.get_sub_total() - self.discount or 0).quantize(
            Decimal("0.01")
        )

    def get_igv(self):
        return Decimal(self.get_total_not_igv() * Decimal(0.18) or 0).quantize(
            Decimal("0.01")
        )

    def get_total_igv(self):
        return Decimal(self.get_total_not_igv() + self.get_igv() or 0).quantize(
            Decimal("0.01")
        )

    def date_cost_quatotion_create(self):
        return self.created.strftime("%Y %-m %-d %H %M %S")

    def date_execution_create(self):
        return self.updated.strftime("%Y %-m %-d %H %M %S")


class OrderItems(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name="order",
        related_name="order_items",
        null=True,
        blank=True,
    )
    characteristictestlab = models.ForeignKey(
        CharacteristicTestLab,
        on_delete=models.SET_NULL,
        verbose_name="characteristictestlab",
        related_name="characteristictestlab_items",
        null=True,
        blank=True,
    )
    test_lab = models.ForeignKey(
        TestLab,
        on_delete=models.SET_NULL,
        verbose_name="test lab",
        related_name="test_lab_items",
        null=True,
        blank=True,
    )
    quantity = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sampling_by = models.BooleanField(null=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self):
        return "(%s): %s - %s" % (self.pk, self.order, self.test_lab)

    def get_partial_igv(self):
        return Decimal(self.price * self.quantity).quantize(
            Decimal("0.01"), rounding=ROUND_UP
        )


class OrderInfo(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, related_name="order_info"
    )
    responsible = models.CharField(
        max_length=15, choices=TypeResponsible.choices, default=TypeResponsible.CLIENT
    )
    riic = models.TextField(
        default="NO SE TIENEN REQUISITOS PARA EL INGRESO",
        blank=True,
        null=True,
        help_text="Información aplicable solo cuando el muestreo es responsabilidad del laboratorio",
    )
    remseg = models.TextField(blank=True, null=True)
    rlras = models.CharField(
        max_length=20,
        choices=TypeLegalRequirements.choices,
        default=TypeLegalRequirements.NO_INDICA,
    )
    observation = models.TextField(blank=True, null=True)
    rirs = models.ForeignKey(
        AdminProfile,
        on_delete=models.SET_NULL,
        related_name="rirs_orderinfo",
        verbose_name="rirs_order_info",
        default=None,
        null=True,
        blank=True,
    )
    recl = models.ForeignKey(
        AdminProfile,
        on_delete=models.SET_NULL,
        related_name="recl_orderinfo",
        verbose_name="recl_orderinfo",
        default=None,
        null=True,
        blank=True,
    )

    def __str__(self):
        return "(%s): (%s)" % (self.pk, self.order)
