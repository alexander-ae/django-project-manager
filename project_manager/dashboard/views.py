# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from projects.models import Project


@login_required
def dashboard(request):
    projects = Project.objects.all()

    return render(request, 'dashboard/dashboard.html', locals())
