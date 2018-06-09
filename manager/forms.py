from django import forms
from fp_app.models import Person, AddedPoints

class PointsForm(forms.ModelForm):
    class Meta():
        model = AddedPoints
        fields = ('description','awarded_points','person')
