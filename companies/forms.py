from django import forms

from .models import Company


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['social_reason', 'address', 'ruc']
        widgets = {
            'social_reason': forms.TextInput(attrs={'placeholder': 'Razón Social', 'autofocus': True, }),
            'address': forms.TextInput(attrs={'placeholder': 'Dirección'}),
            'ruc': forms.TextInput(attrs={'placeholder': 'RUC'}),
        }

    def clean_ruc(self):
        cleaned_data = self.cleaned_data
        ruc = cleaned_data.get['ruc']
        qs = Company.objects.filter(ruc__exact=ruc)
        if qs.exists():
            # self.add_error('ruc', 'This RUC is taken.')
            raise forms.ValidationError('This RUC is taken')
        return ruc
