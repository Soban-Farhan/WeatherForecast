from dotenv import load_dotenv
load_dotenv()

from django.shortcuts import render
from django.http import JsonResponse
import datetime, requests, os

def index(request):

    date = datetime.datetime.now().strftime("%A %d, %B %Y")

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
