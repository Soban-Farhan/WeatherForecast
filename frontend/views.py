from django.shortcuts import render, redirect
import json
import datetime

def index(request):
    date = datetime.datetime.now()
    # day = ["Monday", "Tuesday", "Wednesday", "Thursday", 
    #         "Friday", "Saturday", "Sunday"]
    # month = ["January", "February", "March", "April", "May",
    #         "June", "July", "August", "September", "October",
    #         "November", "December"]
    data = date.strftime("%A %d, %B %Y")
    return render(request, 'index.html', { 'date': data })
# Create your views here.
