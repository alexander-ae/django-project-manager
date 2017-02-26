# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models

from core.utils import ExtendedEnum
from core.models import AuditableModel, Attachment
from projects.models import Project


class IssueStatus(ExtendedEnum):
    ''' Lista de posibles estados de una incidencia '''

    # incidencia pendiente
    New = (0, 'Nuevo')
    Open = (1, 'Abierto')
    Assign = (2, 'Asignado')
    Re_opened = (3, 'Re-abierto')
    In_progress = (4, 'En progreso')

    # incidencia cerrada
    Closed = (10, 'Resuelto')
    Wont_fix = (11, u'No se resolverá')  # no vale la pena la resolución
    Duplicate = (12, 'Duplicado')
    Not_reproducible = (13, 'No reproducible')  # no se puede reproducir
    Not_a_bug = (14, 'No es un error')


class IssuePriority(ExtendedEnum):
    ''' Lista de prioridades en una incidencia '''

    Low = (0, 'Baja')
    Medium = (1, 'Media')
    Hight = (2, 'Alta')


class Issue(AuditableModel):
    name = models.CharField('Asunto', max_length=180)
    details = models.TextField('Detalle', null=True, blank=True)

    project = models.ForeignKey(Project, verbose_name='Proyecto', on_delete=models.SET_NULL, blank=True, null=True)
    status = models.IntegerField('Estado', choices=IssueStatus.choices(), default=IssueStatus.New.value[0])
    priority = models.IntegerField('Prioridad', choices=IssuePriority.choices(), default=IssuePriority.Low.value[0])
    assigned_to = models.ForeignKey(User, verbose_name='Asignado a', on_delete=models.SET_NULL, blank=True, null=True,
                                    related_name='assigned_issues')

    class Meta:
        verbose_name = 'Incidencia'
        verbose_name_plural = 'Incidencias'

    def __str__(self):
        return self.name


class IssueAttachment(Attachment):
    ''' Archivo adjunto de una incidencia '''

    issue = models.ForeignKey(Issue, related_name='issue_attachments')
