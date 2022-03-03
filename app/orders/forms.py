from django import forms
from django.forms import inlineformset_factory

from orders.models import Order, OrderItems, OrderInfo
from companies.models import Company
from members.models import ClientProfile
from projects.models import Project
from tests_labs.models import CharacteristicTestLab, TestLab


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "company",
            "project",
            "client",
            "discount",
            "cost_quatotion",
            "requirement",
            "execution_order",
            "liquidation",
            "type_service",
        )
        labels = {
            "company": "Compañía",
            "project": "Proyecto",
            "client": "Cliente",
            "discount": "Descuento",
            "cost_quatotion": "Cotización",
            "requirement": "Requerimiento",
            "execution_order": "Orden de ejecucón",
            "liquidation": "Liquidación",
            "type_service": "Tipo de Servicio",
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["project"].queryset = Project.objects.none()
    #     self.fields["client"].queryset = ClientProfile.objects.none()

    #     if "company" in self.data:
    #         try:
    #             company_id = int(self.data.get("main-company"))
    #             self.fields["project"].queryset = Project.objects.filter(
    #                 company_id=company_id
    #             ).order_by("name")
    #             self.fields["client"].queryset = ClientProfile.objects.filter(
    #                 company_id=company_id
    #             ).order_by("name")
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         print("running:", self.instance.pk)
    #         self.fields["project"].queryset = self.instance.company.project_set.all()
    #         print("running:", self.fields["project"].queryset)
    #         self.fields[
    #             "client"
    #         ].queryset = self.instance.company.clientprofile_set.all()
    #         print("running:", self.fields["client"].queryset)


class OrderItemsForm(forms.ModelForm):
    required_css_class = "required"

    id = forms.IntegerField()

    class Meta:
        model = OrderItems
        fields = (
            "order",
            "id",
            "characteristictestlab",
            "test_lab",
            "quantity",
            "price",
            "sampling_by",
        )
        labels = {
            "characteristictestlab": "Lab.",
            "test_lab": "Ensayo",
            "quantity": "Cantidad",
            "price": "Precio",
            "sampling_by": "Muestreo por RPG",
        }

    def __init__(self, *args, **kwargs):
        super(OrderItemsForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

        self.fields["id"].label = ""
        self.fields["id"].widget = forms.HiddenInput()

        self.fields["order"].label = ""
        self.fields["order"].widget = forms.HiddenInput()

        # self.fields['test_lab'].queryset = TestLab.objects.none()

        self.fields["price"].widget.attrs["step"] = 0.01


OrderItemsFormset = inlineformset_factory(
    Order,
    OrderItems,
    form=OrderItemsForm,
    extra=0,
    can_delete=False,
    min_num=1,
    validate_min=True,
)


class OrderInfoForm(forms.ModelForm):
    class Meta:
        model = OrderInfo
        fields = (
            "responsible",
            "riic",
            "remseg",
            "rlras",
            "observation",
            "rirs",
            "recl",
        )
        labels = {
            "responsible": "Responsable del muestreo.",
            "riic": "Requisitos para el ingreso a las instalaciones del cliente.",
            "remseg": "Requisitos de los estudios de mecánica de suelos o estudios geotécnico",
            "rlras": "Requisitos legales o reglamentarios aplicables al servicio",
            "observation": "Observaciones",
            "rirs": "Responsable de la identificación de los requisitos del servicio",
            "recl": "Responsable de la evaluación de la capacidad del laboratorio",
        }
        widgets = {
            "riic": forms.Textarea(attrs={"rows": 4}),
            "remseg": forms.Textarea(attrs={"rows": 4}),
            "observation": forms.Textarea(attrs={"rows": 4}),
            "summary": forms.Textarea(attrs={"rows": 4}),
        }
