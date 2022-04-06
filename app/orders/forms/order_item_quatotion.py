from django import forms
from django.forms import inlineformset_factory

from orders.models import OrderQuatotion, OrderItemQuatotion


class OrderItemQuatotionForm(forms.ModelForm):
    class Meta:
        model = OrderItemQuatotion
        fields = (
            "characteristic_testlab",
            "testlab",
            "unit",
            "quantity",
            "price",
            "sampling_by",
            "obs",
        )
        labels = {
            "characteristic_testlab": "Lab.",
            "testlab": "Ensayo",
            "unit": "Ud.",
            "quantity": "Cantidad",
            "price": "S/.",
            "sampling_by": "Muestreo por RPG",
            "obs": "Observaciones",
        }
        widgets = {
            "obs": forms.Textarea(attrs={"rows": 1}),
        }


OrderItemQuatotionFormset = inlineformset_factory(
    OrderQuatotion,
    OrderItemQuatotion,
    form=OrderItemQuatotionForm,
    extra=10,
)
