from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('admission/', views.admission, name='admission'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('pharmacy/', views.pharmacy, name='pharmacy'),
    path('nursing/', views.nursing, name='nursing'),
    path('pysiotherapy/', views.pysiotherapy, name='pysiotherapy'),
]
