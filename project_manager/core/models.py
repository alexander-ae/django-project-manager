# -*- coding: utf-8 -*-

from django.db import models
from uuslug import uuslug
from django.contrib.auth.models import User


class Attachment(models.Model):

    ''' Archivo Adjunto.'''

    attachment = models.FileField(upload_to="attachments/", help_text="(optional)")
    filename = models.CharField('Nombre del archivo', max_length=120)
    details = models.TextField('Detalle', help_text='Opcional', blank=True)

    class Meta:
        verbose_name = 'Archivo Adjunto'
        verbose_name_plural = 'Archivos Adjuntos'
        abstract = True

    def __unicode__(self):
        self.filename


class AuditableModel(models.Model):

    ''' Modelo abstracto utilizado para realizar auditorías '''

    created = models.DateTimeField('Fecha/Hora de creación', auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="%(app_label)s_%(class)s_created_related")
    modified = models.DateTimeField('Fecha/Hora de última actualización', auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="%(app_label)s_%(class)s_modified_related")

    class Meta:
        abstract = True


class SlugModel(models.Model):

    ''' Modelo abstracto utilizado para manejar el campo slug '''

    name = models.CharField('Nombre', max_length=120)
    slug = models.SlugField('Slug', max_length=180, blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(SlugModel, self).save(*args, **kwargs)
