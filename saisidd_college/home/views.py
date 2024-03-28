from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import contacts, admissions
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')

def gallery(request):
    return render(request, 'gallery.html')

def pharmacy(request):
    return render(request, 'pharmacy.html')

def nursing(request):
    return render(request, 'nursing.html')

def pysiotherapy(request):
    return render(request, 'pysiotherapy.html')

def contact(request):
    if request.method == 'POST':
        contact_name = request.POST.get('name')
        contact_email = request.POST.get('email')
        contact_phone = request.POST.get('phone')
        contact_subject = request.POST.get('subject')
        contact_message = request.POST.get('message')

        # Check if the email already exists
        if contacts.objects.filter(contact_email=contact_email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'contact.html', {'name': contact_name, 'email': contact_email, 'phone': contact_phone, 'subject': contact_subject, 'message': contact_message})

        # Create and save the contact object
        contact = contacts.objects.create(
            contact_name=contact_name,
            contact_email=contact_email,
            contact_phone=contact_phone,
            contact_subject=contact_subject,
            contact_message=contact_message,
        )

        # Send email
        send_mail(
            'Contact Form Submission of SaiSidd',
            f'Name: {contact_name}\nEmail: {contact_email}\nPhone: {contact_phone}\nSubject: {contact_subject}\nMessage: {contact_message}',
            contact_email,  # From email (user's email address)
            # settings.EMAIL_HOST_USER,  # From email (configured in settings.py)
            ['sticknobillshafis@gmail.com'],  # To email
            fail_silently=False,
        )

        messages.success(request, 'Your message has been stored successfully .')
        return redirect('contact')
    return render(request, 'contact.html')

def admission(request):
    if request.method == 'POST':
        admission_name = request.POST.get('name')
        admission_number = request.POST.get('phone')
        admission_email = request.POST.get('email')
        admission_state = request.POST.get('state')
        admission_city = request.POST.get('city')
        admission_pincode = request.POST.get('pincode')
        admission_department = request.POST.get('department')

        # Check if the email already exists
        if admissions.objects.filter(admission_email=admission_email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'admission.html', {'name': admission_name, 'email': admission_email, 'phone': admission_number, 'state': admission_state, 'city': admission_city, 'pincode': admission_pincode,'department': admission_department})

        # Create and save the contact object
        admission = admissions.objects.create(
            admission_name = admission_name,
            admission_number = admission_number,
            admission_email = admission_email,
            admission_state = admission_state,
            admission_city = admission_city,
            admission_pincode = admission_pincode,
            admission_department = admission_department,
        )

        # Send email
        send_mail(
            'Admission Form Submission of SaiSidd',
            f'Name: {admission_name}\nEmail: {admission_email}\nPhone: {admission_number}\nState: {admission_state}\nCity: {admission_city}\nPincode: {admission_pincode}\nDepartment: {admission_department}',
            admission_email,
            # settings.EMAIL_HOST_USER,  # From email (configured in settings.py)
            ['sticknobillshafis@gmail.com'],  # To email
            fail_silently=False,
        )

        messages.success(request, 'Your message has been send successfully .')
        return redirect('admission')
    return render(request, 'admission.html')
