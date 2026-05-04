from django.http import HttpResponse
from django.shortcuts import render

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

        print(f"passengers :===> {passengers}")
        print(f"non-passengers :==> {non_passengers}")

        return render(request, 'flight/flight.html', {
                'flight': flight, 
                'passengers': passengers,
                'non_passengers': non_passengers
        })
                    
    
    except Flight.DoesNotExist:
        return HttpResponse(f"Flight id {flight_id} does not exists in our system yet!")
    

def book(request, flight_id):
    pass 