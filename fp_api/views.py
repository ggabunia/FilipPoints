from django.shortcuts import render
from django.contrib.auth.models import User

from . import serializers
from fp_app import models
from rest_framework import mixins, generics, permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.db.models import Count

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'people': reverse('fp_api:people_list', request=request, format=format),
        'points': reverse('fp_api:points', request=request, format=format),
        'add person': reverse('fp_api:add_person', request=request, format=format),
        'add points': reverse('fp_api:add_points', request=request, format=format),
        'points': reverse('fp_api:points', request=request, format=format),
        'update person': reverse('fp_api:update_person', request=request, format=format),
    })

class PeopleView(generics.ListAPIView):

    serializer_class = serializers.PeopleSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        count = None
        try:
            count = self.kwargs['count']
        except:
            count = None
        queryset = models.Person.objects.all().order_by('-points')
        if count is not None and count > 0:
            queryset  = queryset[:count]
        return queryset


class PointsView(generics.ListAPIView):

    serializer_class = serializers.PointsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        count = None
        try:
            count = self.kwargs['count']
        except:
            count = 5

        queryset = models.AddedPoints.objects.values_list('awarded_points').annotate(frequency=Count('awarded_points')).order_by('-frequency').values('awarded_points').distinct()[:count]
        return queryset


class PersonInsertView(generics.CreateAPIView):
    serializer_class = serializers.PeopleSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Person.objects.all()

class AddPointsView(generics.CreateAPIView):
    serializer_class = serializers.AddPointsSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UpdatePerson(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.PeopleSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Person.objects.all()
    lookup_field = 'pk'
