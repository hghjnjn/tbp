# farmers/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm

class FarmerRegistrationForm(UserCreationForm):
    state = forms.CharField(max_length=50)
    location = forms.CharField(max_length=100)

class FarmerLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ChooseStateForm(forms.Form):
    STATES_CHOICES = [
        ('state1', 'State 1'),
        ('state2', 'State 2'),
        # Add more state choices as needed
    ]

    state = forms.ChoiceField(choices=STATES_CHOICES, label='Select State')