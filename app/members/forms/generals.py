from django import forms


class AuthenticationForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'name': 'email'}),
        label='Dirección Email')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password'}),
        strip=False,
        label="Contraseña")

    class Meta:
        fields = ['email', 'password']
