from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect

from HospitalSelect.forms import HospitalForm
from .models import Hospital


# Create your views here.
def home(request):
    return render(request, 'website/indexx.html')


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


def contact(request):
    return render(request, 'website/contact.html')


def login(request):
    return render(request, 'website/login.html')

def registerAccount(request):
    return render(request, 'website/registerAccount.html')
