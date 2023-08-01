from django.shortcuts import render, HttpResponse
from datetime import datetime, date, timedelta
from home.models import info
from django.contrib import messages

# Create your views here.
def index(request):
    return HttpResponse("Tbis is home page")
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def contact(request):
    return render(request, 'contact.html')
def template(request):
    return render(request, 'index.html')
def booking(request):
    return render(request, 'booking.html')
def places(request):
    return render(request,'places.html')
def forms(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile_no=request.POST.get('mobile_no')
        fr=request.POST.get('fr')
        to=request.POST.get('to')
        room=request.POST.get('room')

        fr_date = datetime.strptime(fr, "%Y-%m-%d").date()
        to_date = datetime.strptime(to, "%Y-%m-%d").date()
        current_date = date.today()
        max_date = current_date.replace(year=current_date.year + 1)

        if fr_date < current_date or to_date < current_date or fr > to:  # Date is in the past or invalid date range
            messages.error(request, "Invalid date.")
        elif fr_date > max_date:  # Booking date is more than a year in advance
            messages.error(request, "We don't accept bookings more than a year in advance.")
        elif (to_date - fr_date) > timedelta(days=90):  # Check if difference is more than 3 months (90 days)
            messages.error(request, "We don't accept bookings for more than 3 months.")
        elif len(mobile_no) > 10:
            messages.error(request, "Invalid phone number: Phone number should not exceed 10 digits.")
        else:
            # Check if the selected room type and date range have reached the booking limit
            room_types = ["deluxe", "suite", "executive_suite", "family_room", "presidential_suite"]
            for room_type in room_types:
                existing_bookings = info.objects.filter(room=room_type)
                count = 0  # To keep track of the number of rooms booked for each type
                for booking in existing_bookings:
                    if (fr_date <= booking.to and to_date >= booking.fr) or (to_date >= booking.fr and fr_date <= booking.to) or(fr_date==booking.fr and to_date==booking.to):
                        count += 1  # Increment count if there is an overlap with an existing booking
                    if count >= 5:
                        messages.error(request, f"Sorry, bookings for {room_type.replace('_', ' ').title()} are full for the selected date range.")
                        break
                if count < 5:
                    # Dates are valid and room type is available, save the info object
                    inf = info(name=name, email=email, mobile_no=mobile_no, fr=fr, to=to, room=room)
                    inf.save()
                    messages.success(request, "Booking Done")
                    break
            # If the loop completes without breaking, it means the booking was not made for any room type
            else:
                messages.error(request, "Sorry, there are no available rooms for the selected date range.")

    return render(request, 'bookingform.html')
