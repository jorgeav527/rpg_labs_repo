from django import forms
from django.forms import inlineformset_factory

from orders.models import OrderExecution, OrderItemExecution


class OrderItemExecutionForm(forms.ModelForm):
    class Meta:
        model = OrderItemExecution
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


OrderItemExecutionFormset = inlineformset_factory(
    OrderExecution,
    OrderItemExecution,
    form=OrderItemExecutionForm,
    extra=10,
)
