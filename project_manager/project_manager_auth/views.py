# -*- coding: utf-8 -*-

import logging

from django.contrib.auth import login as auth_login
from django.contrib.auth.views import logout_then_login
from django.shortcuts import render, redirect
from django.utils import timezone


from .constants import DASHBOARD_URL, LOGIN_URL
from .forms import LoginForm

log = logging.getLogger(__name__)


def login(request):
    """ View que permite iniciar sesión """

    if request.user.is_authenticated():
        return redirect(DASHBOARD_URL)

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = form.auth()

            if user is not None:
                if user.is_active:
                    user.last_login = timezone.now()
                    user.save()
                    auth_login(request, user)

                    location = request.GET.get('next', None)

                    if location:
                        return redirect(location)

                    return redirect(DASHBOARD_URL)
                else:
                    form.add_error(None, 'El usuario no se encuentra activo')
            else:
                form.add_error(None, u'Las credenciales son inválidas')
    else:
        form = LoginForm()

    return render(request, 'project_manager_auth/login.html', locals())


def logout(request):
    """ Cierra la sesión del usuario y redirecciona al login """

    return logout_then_login(request, LOGIN_URL)
