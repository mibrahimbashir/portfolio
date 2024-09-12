from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name="home"),
	path("project-1/", views.project_1, name="project-1"),
	path("project-2/", views.project_1, name="project-2"),
	path("project-3/", views.project_1, name="project-3"),
]