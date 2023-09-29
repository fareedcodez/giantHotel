from django.shortcuts import render

def home(request,template_name='pages/index.html'):
    return render (request, template_name=template_name)

def roomDetails(request,template_name='giantHotelApp/roomDetails.html'):
    return render (request, template_name=template_name)

def rooms(request,template_name='giantHotelApp/rooms.html'):
    return render (request, template_name=template_name)

def contactUs(request,template_name='pages/contactUs.html'):
    return render (request, template_name=template_name)

def aboutUs(request,template_name='giantHotelApp/aboutUs.html'):
    return render (request, template_name=template_name)