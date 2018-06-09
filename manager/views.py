from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView,CreateView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from braces.views import SelectRelatedMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, redirect_lazy

from fp_app import models
from . import forms

class PersonCreate(LoginRequiredMixin,CreateView):
    model = models.Person
    fields = ('first_name', 'last_name')
    template_name = 'manager/new_person.html'

class PersonEdit(LoginRequiredMixin,UpdateView):
    model = models.Person
    fields = ('first_name', 'last_name')
    template_name = 'manager/edit_person.html'

class AddPoints(LoginRequiredMixin,TemplateView):
    def get(self,request, **kwargs):
        pk = self.kwargs['pk']
        person = models.Person.objects.get(pk=pk)
        form = forms.PointsForm()
        return render(request, 'manager/add_points.html', context = {'person': person, 'form': form})
    def post(self,request, **kwargs):
        form = forms.PointsForm(request.POST)
        if form.is_valid():
            form.save()
            return red
