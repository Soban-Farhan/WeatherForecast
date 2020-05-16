from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import json
import datetime
import requests
import os

def index(request):

    date = datetime.datetime.now().strftime("%A %d, %B %Y")
    day = ["Monday", "Tuesday", "Wednesday", "Thursday", 
            "Friday", "Saturday", "Sunday"]

    # month = ["January", "February", "March", "April", "May",
    #         "June", "July", "August", "September", "October",
    #         "November", "December"]
    #   
    if request.method == "POST":

        url = "https://api.weatherapi.com/v1/forecast.json"
        param = {
            'key': os.environ['key'],
            'q': request.POST.get('cities'),
            'days': '5',
        }

        data = requests.get(url, param)
        data = data.json()

        return render(request, 'index.html', { 'date': date, 'data': data })
        # return HttpResponse()

    return render(request, 'index.html', { 'date': date })

def ping(request):
    return JsonResponse({'status':'true'}, status=200)
# Create your views here.
