from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('projects/<str:pk>/', views.singleProject, name='single-projects'),
    path('create-project/', views.createProject, name='create-project'),
]