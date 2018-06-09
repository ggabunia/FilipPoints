from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView,CreateView
from django.http import HttpResponse, HttpResponseRedirect
from braces.views import SelectRelatedMixin, PrefetchRelatedMixin
from . import models


class Index(ListView):
    model = models.Person
    ordering = ['-points']
    template_name = 'fp_app/index.html'

class PersonList(ListView):
    model = models.Person
    ordering = ['-points']


class PersonDetail(DetailView):
    model = models.Person
