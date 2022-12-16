from django.contrib import admin

from .models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = 'title',
    list_display_links = 'title',
    search_fields = 'title',
