from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin, TreeRelatedFieldListFilter

from .models import department, team, teams

# Register your models here.

admin.site.register(department)


@admin.register(team)
class teamAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 't_parent', 't_level')
    search_fields = ('name',)
    ordering = ['-t_level']
    list_filter = ('department', 't_level', 't_parent',)


@admin.register(teams)
class teamsAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions',
                    'indented_title', 'name', 'department', 'parent', 'level')
    search_fields = ('name',)
    # ordering = ['tree_id']
    list_filter = ('department', ('parent', TreeRelatedFieldListFilter))
    mptt_level_indent = 15
