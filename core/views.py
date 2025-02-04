from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,"core/index.html")

def car_view(request):
    return render(request, "car_view\car_view.html")