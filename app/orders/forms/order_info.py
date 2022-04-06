from django import forms

from orders.models import OrderInfo


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
            "question_1",
            "question_2",
            "question_3",
            "question_4",
            "question_5",
            "question_6",
            "question_7",
            "question_8",
            "obs",
        )
        labels = {
            "responsible": "Responsable del muestreo.",
            "riic": "Requisitos para el ingreso a las instalaciones del cliente.",
            "remseg": "Requisitos de los estudios de mecánica de suelos o estudios geotécnico",
            "rlras": "Requisitos legales o reglamentarios aplicables al servicio",
            "observation": "Observaciones",
            "rirs": "Responsable de la identificación de los requisitos del servicio",
            "recl": "Responsable de la evaluación de la capacidad del laboratorio",
            "question_1": "1.-¿El Laboratorio tiene capacidades para aplicar el método requerido?",
            "question_2": "2.-¿El Laboratorio cuenta con el equipo necesario para realizar el servicio?",
            "question_3": "3.-¿El Laboratorio cuenta con personal competente y disponible para realizar el servicio?",
            "question_4": "4.-¿El Laboratorio dispone del tiempo suficiente para realizar el servicio?",
            "question_5": "5.-¿Es necesario subcontratar la totalidad o parte del servicio?",
            "question_6": "6.-¿El método a utilizar es apropiado para el servicio solicitado?",
            "question_7": "7.-¿El servicio ofrecido está acreditado?",
            "question_8": "8.-¿En términos generales, el laboratorio cuenta con la capacidad para cumplir con los requisitos de los servicios?",
            "obs": "Observaciones",
        }
        widgets = {
            "riic": forms.Textarea(attrs={"rows": 4}),
            "remseg": forms.Textarea(attrs={"rows": 4}),
            "observation": forms.Textarea(attrs={"rows": 4}),
            "summary": forms.Textarea(attrs={"rows": 4}),
            "obs": forms.Textarea(attrs={"rows": 4}),
        }
        help_texts = {
            "question_5": "(Indicar en el campo observaciones el motivo y el servicio que se requiere contratar).",
        }
