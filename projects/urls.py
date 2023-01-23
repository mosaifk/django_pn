from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.ProjectListView.as_view(), name="project_list"),
    path("project/create", views.ProjectListView.as_view(), name="project_create")

]