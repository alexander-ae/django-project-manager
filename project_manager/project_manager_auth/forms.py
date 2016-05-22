# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):

    ''' Formulario de acceso al sistema '''

    username = forms.CharField(label='Usuario / Email')
    username.widget.attrs.update({'autofocus': 'true', 'tabindex': '1'})

    password = forms.CharField(label='Contraseña', min_length=6,
        max_length=32, widget=forms.PasswordInput)
    password.widget.attrs.update({'tabindex': '2'})

    def clean_username(self):
        username = self.cleaned_data['username']
        # verificamos si lo ingresado es el nombre de un usuario o un correo
        if '@' in username:
            try:
                user = User.objects.get(email=username)
                return user.username
            except User.DoesNotExist:
                mensaje = u'El correo no ha sido registrado'
                raise forms.ValidationError(mensaje)
        else:
            try:
                User.objects.get(username=username)
                return username
            except User.DoesNotExist:
                mensaje = u'El usuario no ha sido registrado'
                raise forms.ValidationError(mensaje)

    def auth(self):
        cd = self.cleaned_data
        return authenticate(username=cd['username'], password=cd['password'])
