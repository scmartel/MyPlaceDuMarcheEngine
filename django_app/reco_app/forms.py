from django import forms
from .models import User_input


## this is the code from the tutorial that does not seem to be working


# Create your views here.
# import rest_framework
# from rest_framework import fields, serializers
from django import forms
from reco_app.models import location_choices, service_size_choices, organization_size_choices, role_choices, organization_types


class userinput_form(forms.Form):
    # ...
    # locations = forms.MultipleChoiceField(choices=location_choices, widget=forms.CheckboxSelectMultiple)
    locations = forms.CharField(label='Select a desired location', widget=forms.Select(choices=location_choices))
    services = forms.MultipleChoiceField(label='Select service choices', choices=service_size_choices, widget=forms.CheckboxSelectMultiple)
    organizations = forms.MultipleChoiceField(label='Select organization size choices', choices=organization_size_choices, widget=forms.CheckboxSelectMultiple)
    roles = forms.MultipleChoiceField(label='Select desired roles', choices=role_choices, widget=forms.CheckboxSelectMultiple)
    # ...

## this is another attempt at a model form --  this one works

'''
from django import forms
from reco_app.models import location_choices, service_size_choices, organization_size_choices, role_choices

class userinput_form(forms.Form):
    locations = forms.CharField(label='Select a desired location', widget=forms.Select(choices=location_choices))
    services = forms.CharField(label='Select service choices', widget=forms.Select(choices=service_size_choices))
    organizations = forms.CharField(label='Select organization size choices', widget=forms.Select(choices=organization_size_choices))
    roles = forms.CharField(label='Select desired roles', widget=forms.Select(choices=role_choices))
'''

# Organization Form - not needed for now
'''
class organization_form(forms.Form):
    name = forms.CharField(label='Enter organization name')
    locations = forms.CharField(label='Select a desired location', widget=forms.Select(choices=location_choices))
    service_size = forms.CharField(label='Select service size', widget=forms.Select(choices=service_size_choices))
    organization_size = forms.CharField(label='Select organization size', widget=forms.Select(choices=organization_size_choices))
    organization_type = forms.CharField(label='Select organization type', widget=forms.Select(choices=organization_types))
    roles = forms.MultipleChoiceField(label='Select desired roles', choices=role_choices, widget=forms.CheckboxSelectMultiple)
'''