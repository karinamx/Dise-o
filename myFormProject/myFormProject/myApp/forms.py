from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'contraseña', 'dirección', 'dirección2', 'ciudad', 'estado', 'código_postal']
        widgets = {
            'contraseña': forms.PasswordInput(),
        }
