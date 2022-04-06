from django import forms

from orders.models import OrderExecution


class OrderExecutionForm(forms.ModelForm):
    class Meta:
        model = OrderExecution
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
