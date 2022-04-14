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

    def clean_quatotion(self):
        quatotion = self.cleaned_data.get("quatotion")
        if self.instance.quatotion != quatotion:
            self.add_error("quatotion", "Debe tener una cotización.")
        return quatotion

    def clean_requirement(self):
        requirement = self.cleaned_data.get("requirement")
        if self.instance.requirement != requirement:
            self.add_error("requirement", "Debe tener un requerimiento.")
        return requirement

    def clean_execution(self):
        execution = self.cleaned_data.get("execution")
        if self.instance.liquidation and not execution:
            self.add_error(
                "execution",
                "No se puede eliminar una orden de ejecución si esta tiene liquidación.",
            )
        return execution
