from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')

def admission(request):
    return render(request, 'admission.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')

def pharmacy(request):
    return render(request, 'pharmacy.html')

def nursing(request):
    return render(request, 'nursing.html')

def pysiotherapy(request):
    return render(request, 'pysiotherapy.html')