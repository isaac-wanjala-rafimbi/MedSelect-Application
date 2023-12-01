from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'county': forms.Select(attrs={'class': 'form-control'}),
            'constituency': forms.Select(attrs={'class': 'form-control'}),
            'specializations': forms.CheckboxSelectMultiple(),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'nhif_coverage': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        }




class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
