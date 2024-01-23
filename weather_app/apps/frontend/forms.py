from django import forms

from .models import CityData, CityDetail

# Form for CityData
class CityDataForm(forms.ModelForm):
    class Meta:
        model = CityData
        exclude = ['created_at', 'updated_at']

# Form for CityDetail
class CityDetailForm(forms.ModelForm):
    class Meta:
        model = CityDetail
        exclude = ['created_at', 'updated_at']