from django import forms
from .models import Person
from .utils import blood_types, gender

class PersonForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Name'}),
    )
    gender = forms.ChoiceField(choices=gender)
    dob = forms.DateField(widget=forms.TextInput(attrs={'placeholder': '2001-01-30'}),)
    blood_type = forms.ChoiceField(choices=blood_types)
    height = forms.DecimalField(
        max_digits=5,
        decimal_places=2,
        widget=forms.TextInput(attrs={'placeholder': 'Height in Cm'}),)
    weight = forms.DecimalField(
        max_digits=5,
        decimal_places=2,
        widget=forms.TextInput(attrs={'placeholder': 'Weight in Kg'}),
    )
