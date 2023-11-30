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


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
