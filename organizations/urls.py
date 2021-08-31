from django.urls import path
from . import views

urlpatterns = [
    path('', views.organizations, name='organizations'),
#    path('projects/', views.projects, name='projects'),
#    path('projects/<int:pk>/', views.project, name='project'),
#    path('create-project', views.createProject, name='create-project'),
#    path('update-project/<int:pk>/', views.updateProject, name='update-project'),
#    path('delete-project/<int:pk>/', views.deleteProject, name='delete-project'),
]
