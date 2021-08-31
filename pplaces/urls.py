from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:pk>/', views.project, name='project'),
    path('create-project', views.createProject, name='create-project'),
    path('update-project/<int:pk>/', views.updateProject, name='update-project'),
    path('delete-project/<int:pk>/', views.deleteProject, name='delete-project'),


    path('fr/projects/<int:pk>/', views.project_fr, name='project-fr'),

    path('create-projectlocation/<int:pk>', views.CreateProjectLocation, name='create-project-location'),
    path('remove-project-location/<int:prj_id>/<int:pl_id>/', views.removeProjectLocation, name="remove-project-location"),
]
