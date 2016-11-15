from django import forms
from formset.models import *


class SetupForm(forms.ModelForm):
    class Meta:
        model = Setup
        fields = '__all__'


class SpecificationForm(forms.ModelForm):
    class Meta:
        model = Specification
        fields = '__all__'
