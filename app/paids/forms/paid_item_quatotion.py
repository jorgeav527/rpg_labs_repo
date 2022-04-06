from django import forms
from django.forms import inlineformset_factory

from orders.models import OrderQuatotion
from paids.models import PaidItemQuatotion


class PaidItemQuatotionForm(forms.ModelForm):
    class Meta:
        model = PaidItemQuatotion
        fields = ("percentage",)
        labels = {
            "percentage": "Porcentaje",
        }


PaidItemQuatotionFormset = inlineformset_factory(
    OrderQuatotion,
    PaidItemQuatotion,
    form=PaidItemQuatotionForm,
    max_num=4,
    extra=4,
)
