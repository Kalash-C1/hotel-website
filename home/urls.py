from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    # path('', views.index, name="Home"),
    path('about', views.about, name="About"),
    path('services', views.services, name="Services"),
    path('contacts', views.contact, name="Contacts"),
    path('', views.template, name='Home'),
    path('booking', views.booking, name="Booking"),
    path('booking_form', views.forms, name="Booking")
]