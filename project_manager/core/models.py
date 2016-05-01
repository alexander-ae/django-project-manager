# -*- coding: utf-8 -*-

from django.db import models
from uuslug import uuslug


class SlugModel(models.Model):
    ''' Modelo abstracto para manejar el campo slug '''
    name = models.CharField('Nombre', max_length=120)
    slug = models.SlugField('Slug', max_length=180, blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(SlugModel, self).save(*args, **kwargs)
