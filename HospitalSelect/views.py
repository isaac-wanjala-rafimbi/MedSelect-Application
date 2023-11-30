from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string

from HospitalSelect.forms import HospitalForm, CreateUserForm, ContactForm
from .models import Hospital
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, 'website/indexx.html')


login_required(login_url='login')


def register(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Submitted Successfully')

    else:
        form = HospitalForm()

    return render(request, 'website/register.html', {'form': form})


def find(request):
    qs = Hospital.objects.all()
    county = request.GET.get('county')
    constituency = request.GET.get('constituency')
    specialization = request.GET.get('specializations')

    if county or constituency or specialization:
        # If any search parameter is provided, filter the queryset
        qs = qs.filter(
            Q(county__name__icontains=county) if county else Q(),
            Q(constituency__name__icontains=constituency) if constituency else Q(),
            Q(specializations__name__icontains=specialization) if specialization else Q(),
        ).distinct()

    context = {
        'queryset': qs
    }
    return render(request, 'website/findHospitals.html', context)


def blog(request):
    return render(request, 'website/blog.html')


# def  contact(request):
#  return render(request, 'website/contact.html')


def registerAccount(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'website/registerAccount.html', context)


login_required(login_url='login')


def adminPage(request):
    # Retrieve the hospitals data
    hospitals = Hospital.objects.all()

    # Pass the data to the template
    context = {'hospitals': hospitals}
    return render(request, 'website/adminPage.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin')
        else:
            messages.info(request, 'username OR password is incorrect')

    context = {}
    return render(request, 'website/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('logout')


def update_hospital(request, hospital_id):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    if request.method == 'POST':
        form = HospitalForm(request.POST, instance=hospital)
        if form.is_valid():
            form.save()
            messages.success(request, ('hospital Updated Successfully'))
            return redirect('admin')
            # Handle success or redirection
    else:
        form = HospitalForm(instance=hospital)

    return render(request, 'website/updateHospital.html', {'form': form, 'hospital': hospital})


@login_required(login_url='login')
def delete_hospital(request, hospital_id):
    hospital = Hospital.objects.get(pk=hospital_id)
    # hospital = get_object_or_404(Hospital, id=hospital_id)

    hospital.delete()
    messages.success(request, ('hospital deleted..'))
    return redirect('admin')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                f'Contact Form Submission - {subject}',
                f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}',
                'isaacralph982@gmail.com',
                ['isaacralph982@gmail.com'],

            )

            return render(request, 'website/contact.html')
    else:
        form = ContactForm()

    return render(request, 'website/contact.html', {'form': form})
