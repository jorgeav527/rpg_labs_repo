from django import forms

from orders.models import OrderLiquidation


class OrderLiquidationForm(forms.ModelForm):
    class Meta:
        model = OrderLiquidation
        fields = (
            "discount",
            "observation",
        )
        labels = {
            "discount": "Descuento",
            "observation": "Observaciones",
        }
        widgets = {
            "observation": forms.Textarea(attrs={"rows": 1}),
        }
