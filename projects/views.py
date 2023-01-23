from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from . import models
from . import forms
from django.shortcuts import render


class ProjectListView(ListView):
    model = models.Project
    template_name = "project/list.html"


class ProjectCreateView(CreateView):
    modle = models.Project
    form_class = forms.ProjectCreateForm
    template_name = "project/create.html"
    success_url = reverse_lazy("project_list")
