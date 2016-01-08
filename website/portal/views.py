from django.shortcuts import render
from django.http import HttpResponse
from location.models import *
from utilities.config import SCORE_THRESHOLD
import json


def index(request):
    return render(request, 'base.html')

def get_states(request):
    country = request.GET['country']
    country = Country.objects.get(country=country)
    states = State.objects.filter(country=country)
    state_names = []
    for i in range(len(states)):
        state_names.append(states[i].state)
    reply = {'states': state_names}

    return HttpResponse(json.dumps(reply),content_type="application/json")


def get_cities(request):
    state = request.GET['state']
    state = State.objects.get(state=state)
    cities = City.objects.filter(state=state)
    city_names = []
    for i in range(len(cities)):
        city_names.append(cities[i].city)
    reply = {'cities': city_names}

    return HttpResponse(json.dumps(reply),content_type="application/json")


def verify_pincode(request):
    city = request.GET['city']
    pincode = int(request.GET['pincode'])
    city = City.objects.get(city=city)
    validity = False
    if pincode >= city.zip_start and pincode <= city.zip_end:
        validity = True
    reply = {'valid': validity}
    return HttpResponse(json.dumps(reply),content_type="application/json")


def check(request):
    pincode = request.POST['pincode']
    context = {}
    if Pincode.objects.filter(pincode=pincode).exists():
        score = Pincode.objects.get(pincode=pincode).score
    else:
        score = 0.0
    if score < SCORE_THRESHOLD:
        context['blocked'] = True
    else:
        context['blocked'] = False

    context['score'] = score
    context['threshold'] = SCORE_THRESHOLD
    return render(request, 'result.html', context)