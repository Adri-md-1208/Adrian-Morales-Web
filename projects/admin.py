from django.contrib import admin
from .models import Project

class Project_admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Project, Project_admin)

