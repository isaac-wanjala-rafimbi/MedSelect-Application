from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'website/indexx.html')
def register(request):
    return render(request, 'website/register.html')


