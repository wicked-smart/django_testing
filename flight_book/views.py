from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *

# Create your views here.


def index(request):

    flights = Flight.objects.all()

    return render(request, 'flight/index.html', {
        'flights': flights
    })

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(id=flight_id)

        passengers = flight.passengers.all()
        non_passengers = Passenger.objects.exclude(flight=flight)

        # print(f"passengers :===> {passengers}")
        # print(f"non-passengers :==> {non_passengers}")

        return render(request, 'flight/flight.html', {
                'flight': flight, 
                'passengers': passengers,
                'non_passengers': non_passengers
        })
                    
    
    except Flight.DoesNotExist:
        return HttpResponse(f"Flight id {flight_id} does not exists in our system yet!")
    

def book(request, flight_id):

    if request.method == 'POST':
        try:
            pasngr_id  = int(request.POST.get('passenger_id', None))
            passenger = Passenger.objects.get(id=pasngr_id)

            flight = Flight.objects.get(id=flight_id)

            #book passenger
            flight.passengers.add(passenger)
            flight.save()

            return HttpResponseRedirect(reverse('flight', args=(flight_id,)))

        
        except Exception as e:
            print(f"Exception occured during fligh booking :-- {e}")

