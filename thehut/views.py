from django.shortcuts import render, redirect
from .models import Booking


def index(request):
    return render(request, 'index.html')


def booking(request):
    if request.method == 'POST':
        name = request.POST.get('booking_name')
        email = request.POST.get('booking_email')
        phone = request.POST.get('booking_phone')
        num_guests = request.POST.get('booking_num_guests')
        date = request.POST.get('booking_date')
        time = request.POST.get('booking_time')
        Booking.objects.create(
            name=name,
            email=email,
            phone=phone,
            num_guests=num_guests,
            date=date,
            time=time,
        )
        return redirect('index')
    return render(request, 'booking.html')
