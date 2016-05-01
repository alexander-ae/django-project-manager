# -*- coding: utf-8 -*-

from core.models import SlugModel


class Project(SlugModel):

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['name']
