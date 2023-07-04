from django import forms
from .models import Vehiculo
from django.forms import ModelForm, forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        def save(self, commit=True):
            user = super(RegistroUsuarioForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
                return user