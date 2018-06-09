from django.shortcuts import render
from django.views.generic import (TemplateView, ListView,
                                    DetailView,CreateView,
                                    UpdateView, DeleteView)
from django.http import HttpResponse, HttpResponseRedirect
from braces.views import SelectRelatedMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from datetime import datetime

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

class DeletePerson(LoginRequiredMixin, DeleteView):
    model = models.Person
    success_url = reverse_lazy('filip_points:all')
    template_name = 'manager/person_confirm_delete.html'

class RemovePoints(LoginRequiredMixin, DeleteView):
    model = models.AddedPoints
    template_name = 'manager/remove_points.html'

    def get_success_url(self):
        person = self.object.person
        return reverse_lazy( 'filip_points:details', kwargs={'pk': person.pk})

    def delete(self, *args, **kwargs):
        object = self.get_object()
        person =object.person
        person.points -= object.awarded_points
        person.save()
        return super().delete(*args, **kwargs)

class AddPoints(LoginRequiredMixin,TemplateView):
    def get(self,request, **kwargs):
        pk = self.kwargs['pk']
        person = get_object_or_404(models.Person,pk=pk)
        return render(request, 'manager/add_points.html', context = {'person': person, })

    def post(self,request, **kwargs):

        points = int(request.POST['awarded_points'])
        description = request.POST['description']
        person_id = int(request.POST.get('person_id'))
        person = get_object_or_404(models.Person,pk = person_id)
        ap = models.AddedPoints(person = person, description = description, awarded_points = points)
        ap.save()
        person.points += points
        person.last_update = datetime.now()
        person.save()
        return redirect(reverse_lazy('filip_points:details', kwargs = {'pk': person_id}))
