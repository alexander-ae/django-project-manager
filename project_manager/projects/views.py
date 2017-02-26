from django.shortcuts import render, redirect
from .forms import ProjectNewEditForm
from .models import Project


def new_edit(request, slug=None):
    if slug:
        instance = Project.objects.get(slug=slug)
    else:
        instance = Project()

    if request.method == 'POST':
        form = ProjectNewEditForm(request.POST, instance=instance)
        if form.is_valid():
            new_instance = form.save()

            return redirect(new_instance.get_absolute_url())
    else:
        form = ProjectNewEditForm(instance=instance)

    return render(request, 'projects/new_edit.html', locals())
