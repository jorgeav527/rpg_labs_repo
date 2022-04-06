from django import forms
from django.forms import inlineformset_factory

from orders.models import OrderLiquidation, OrderItemLiquidation


class OrderItemLiquidationForm(forms.ModelForm):
    class Meta:
        model = OrderItemLiquidation
        fields = (
            "characteristic_testlab",
            "testlab",
            "unit",
            "quantity",
            "price",
            "sampling_by",
        )
        labels = {
            "characteristic_testlab": "Lab.",
            "testlab": "Ensayo",
            "unit": "Ud.",
            "quantity": "Cantidad",
            "price": "S/.",
            "sampling_by": "Muestreo por RPG",
        }


OrderItemLiquidationFormset = inlineformset_factory(
    OrderLiquidation,
    OrderItemLiquidation,
    form=OrderItemLiquidationForm,
    extra=10,
)
