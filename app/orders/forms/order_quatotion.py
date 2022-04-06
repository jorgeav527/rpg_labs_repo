from django import forms

from orders.models import OrderQuatotion


class OrderQuatotionForm(forms.ModelForm):
    class Meta:
        model = OrderQuatotion
        fields = (
            "company",
            "project",
            "client",
            "discount",
            "quatotion",
            "requirement",
            "execution",
            "liquidation",
            "type_service",
            "observation",
        )
        labels = {
            "company": "Compañía",
            "project": "Proyecto",
            "client": "Cliente",
            "discount": "Descuento",
            "quatotion": "Cotización",
            "requirement": "Requerimiento",
            "execution": "Orden de ejecucón",
            "liquidation": "Liquidación",
            "type_service": "Tipo de Servicio",
            "observation": "Observaciones",
        }
        widgets = {
            "observation": forms.Textarea(attrs={"rows": 1}),
        }
