from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model
from members.choices import Roles

USER = get_user_model()


class AdminSignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label="Contraseña",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text="Escriba una contraseña.",
    )
    password2 = forms.CharField(
        label="Confirmación Contraseña",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text="Digite la misma contraseña.",
    )

    class Meta:
        model = USER
        fields = [
            "email",
            "first_name",
            "last_name",
            "dni",
            "profession",
            "cell_phone",
            "password1",
            "password2",
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
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
                "autofocus"
            ] = False

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2
