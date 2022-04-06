from django import forms
from django.forms import inlineformset_factory

from orders.models import OrderExecution
from paids.models import PaidItemExecution


class PaidItemExecutionForm(forms.ModelForm):
    class Meta:
        model = PaidItemExecution
        fields = ("percentage",)
        labels = {
            "percentage": "Porcentaje",
        }


PaidItemExecutionFormset = inlineformset_factory(
    OrderExecution,
    PaidItemExecution,
    form=PaidItemExecutionForm,
    max_num=4,
    extra=4,
)
