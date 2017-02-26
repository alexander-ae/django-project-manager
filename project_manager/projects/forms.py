from django import forms
from .models import Project


class ProjectNewEditForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name']
