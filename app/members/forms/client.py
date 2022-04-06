from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


USER = get_user_model()
RAW_PASSWORD = "rpgclient123"


class ClientSignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.HiddenInput())
    password2 = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = USER
        fields = [
            "email",
            "first_name",
            "last_name",
            "dni",
            "profession",
            "cell_phone",
        ]
        labels = {
            "email": "Dirección Email",
            "first_name": "Nombres",
            "last_name": "Apellidos",
            "dni": "DNI",
            "profession": "Profesión",
            "cell_phone": "Celular",
        }
        help_texts = {
            "email": "Solo correos gmail.",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields["password1"].required = False
            self.fields["password2"].required = False
