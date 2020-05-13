from django.shortcuts import render, redirect
import json
import datetime

def index(request):
    return render(request, 'index.html')
# Create your views here.
