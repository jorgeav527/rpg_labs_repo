from django import forms

from .models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["social_reason", "address", "ruc", "type_company"]
        labels = {
            "social_reason": "Razón Social",
            "address": "Dirección",
            "ruc": "RUC",
            "type_company": "Tipo de Cliente",
        }
        help_texts = {
            "social_reason": "Ingresa el nombre de la empresa.",
            "address": "Ingresa la Dirección fisica de la empresa.",
            "ruc": "Ingresa el RUC de la empresa.",
        }
        error_messages = {
            "ruc": {
                "unique": "El RUC esta en uso.",
            }
        }

    # def clean_ruc(self):
    #     ruc = self.cleaned_data.get("ruc")
    #     qs = Company.objects.filter(ruc__exact=ruc)
    #     if qs.exists():
    #         self.add_error('ruc', 'El RUC esta en uso.')
    #     return ruc
