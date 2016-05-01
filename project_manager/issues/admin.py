# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import IssueAttachment, Issue


class IssueAttachmentInline(admin.TabularInline):
    model = IssueAttachment
    extra = 0


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    inlines = [IssueAttachmentInline]
