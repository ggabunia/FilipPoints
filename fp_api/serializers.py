from django.contrib.auth.models import User
from rest_framework import serializers
from fp_app import models
from django.shortcuts import get_object_or_404
from datetime import datetime




class PeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Person
        fields = ( 'pk','first_name', 'last_name','points')
        read_only_fields = ('pk','points')

class PointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AddedPoints
        fields = ("awarded_points",)


class AddPointsSerializer(serializers.Serializer):

    awarded_points = serializers.IntegerField()
    description = serializers.CharField()
    person_id = serializers.IntegerField()
    datestamp = serializers.IntegerField(write_only = True)
    def create(self, validated_data):
        print(validated_data)
        print(type(validated_data))
        points = int(validated_data['awarded_points'])
        description = validated_data['description']
        person_id = int(validated_data['person_id'])
        person = get_object_or_404(models.Person,pk = person_id)
        d_stamp = int(int(validated_data['datestamp']) / 1000)
        print(d_stamp)
        date_added = datetime.fromtimestamp(d_stamp)
        print(date_added)
        ap = models.AddedPoints(person = person, description = description, awarded_points = points, date = date_added)
        ap.save()
        person.points += points
        if person.last_update.timestamp() < date_added.timestamp():
            person.last_update = date_added
        person.save()
        return ap
