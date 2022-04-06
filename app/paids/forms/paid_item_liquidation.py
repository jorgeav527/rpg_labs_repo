from django import forms
from django.forms import inlineformset_factory

from orders.models import OrderLiquidation
from paids.models import PaidItemLiquidation


class PaidItemLquidationForm(forms.ModelForm):
    class Meta:
        model = PaidItemLiquidation
        fields = ("percentage",)
        labels = {
            "percentage": "Porcentaje",
        }


PaidItemLquidationFormset = inlineformset_factory(
    OrderLiquidation,
    PaidItemLiquidation,
    form=PaidItemLquidationForm,
    max_num=4,
    extra=4,
)
