from django.db import models
from datetime import datetime
from django.urls import reverse

class Person(models.Model):
    first_name = models.CharField(max_length = 256)
    last_name = models.CharField(max_length = 256, blank = True)
    points = models.IntegerField(default = 0)
    last_update = models.DateTimeField(default = datetime.now)

    def get_absolute_url(self):
        return reverse('filip_points:details',kwargs = {'pk':self.pk})

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class AddedPoints(models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='points_history')
    description = models.TextField()
    awarded_points = models.IntegerField()
    date = models.DateTimeField(default = datetime.now)
    class Meta():
        ordering = ['-date']
