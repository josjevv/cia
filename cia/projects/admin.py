from .models import *
from django.contrib import admin
from django.conf import settings

class MilestoneInline(admin.TabularInline):
    model = Milestone

class ProjectAdmin(admin.ModelAdmin):
    inlines = [MilestoneInline,]



admin.site.register(Client)
admin.site.register(Project, ProjectAdmin)
