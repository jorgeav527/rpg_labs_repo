from django.db import models

from members.models import AdminProfile
from orders.choices import TypeResponsible, TypeLegalRequirements
from orders.models import OrderQuatotion


class OrderInfo(models.Model):
    order_quotation = models.OneToOneField(
        OrderQuatotion,
        on_delete=models.CASCADE,
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
    question_1 = models.BooleanField(default=True)
    question_2 = models.BooleanField(default=True)
    question_3 = models.BooleanField(default=True)
    question_4 = models.BooleanField(default=True)
    question_5 = models.BooleanField(default=False)
    question_6 = models.BooleanField(default=True)
    question_7 = models.BooleanField(default=False)
    question_8 = models.BooleanField(default=True)
    obs = models.TextField(blank=True, null=True)

    def __str__(self):
        return "(%s): (%s)" % (self.pk, self.order_quotation)
