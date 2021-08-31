from django.contrib import admin
from .models import Project, PriorityPlacesREF, ProjectLocation

# Register your models here.
#class ProjectLocationInline(admin.TabularInline):
#    model = ProjectLocation
#    extra = 2

#@admin.register(Project)
#class ProjectAdmin(admin.ModelAdmin):
#     inlines = [
#        ProjectLocationInline,
#    ]

admin.site.register(Project)
admin.site.register(PriorityPlacesREF)
admin.site.register(ProjectLocation)