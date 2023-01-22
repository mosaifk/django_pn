from django.views.generic import ListView
from . import models
from django.shortcuts import render


class ProjectListView(ListView):
    model = models.Project
    template_name = "Project/list.html"
