from django.shortcuts import render

def home(request):
    return render (request, 'pages/index.html')

def roomDetails(request):
    return render (request, 'giantHotelApp/roomDetails.html')

def rooms(request):
    return render (request, 'giantHotelApp/rooms.html')

def contactUs(request):
    return render (request, 'pages/contactUs.html')

def aboutUs(request):
    return render (request, 'pages/aboutUs.html')