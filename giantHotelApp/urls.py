from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room-details/', views.roomDetails, name='room-details'),
    path('rooms/', views.rooms, name='rooms'),
    path('contact-us/', views.contactUs, name='contact-us'),
    path('about-us/', views.aboutUs, name='about-us'),
]