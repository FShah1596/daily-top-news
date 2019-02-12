from django.contrib.auth.models import User
from django import forms


class SourceForm(forms.Form):
    category_selected = forms.BooleanField(required=False)
    language_selected = forms.BooleanField(required=False)
    country_selected = forms.BooleanField(required=False)


class EverythingForm(forms.Form):
    q = forms.CharField(max_length=100, required=False)
    domains = forms.CharField(max_length=100, required=False)
    fromTime = forms.DateField(required=False)
    toTime = forms.DateField(required=False)
    language_selected = forms.BooleanField(required=False)
    sortBy = forms.ChoiceField(widget=forms.RadioSelect, required=False)

    # class Meta:
    #     model = User
    #     fields = ['language', 'country', 'category']
#
