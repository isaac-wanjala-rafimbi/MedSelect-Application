from django import forms
from .models import County, Constituency, Specialization, Hospital


class CountyForm(forms.ModelForm):
    class Meta:
        model = County
        fields = ['name']


class ConstituencyForm(forms.ModelForm):
    class Meta:
        model = Constituency
        fields = ['name', 'county']


class SpecializationForm(forms.ModelForm):
    class Meta:
        model = Specialization
        fields = ['name']


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['name', 'county', 'constituency', 'specializations', 'nhif_coverage', 'photo', 'contact_phone',
                  'contact_email', 'country']
