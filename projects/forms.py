from django import forms

from projects.models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name', 'location']
        labels = {
            'name': 'Nombre del Proyecto',
            'location': 'Ubicación del Projecto',
        }
        error_messages = {
            'name': {
                'require': 'El nombre del proyecto es requerido.',
            }
        }

    # def clean_ruc(self):
    #     ruc = self.cleaned_data.get("ruc")
    #     qs = Company.objects.filter(ruc__exact=ruc)
    #     if qs.exists():
    #         self.add_error('ruc', 'El RUC esta en uso.')
    #     return ruc
