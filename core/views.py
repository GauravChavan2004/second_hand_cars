from django.shortcuts import render, redirect



# Create your views here.
def index(request):
    return render(request,"core/index.html")

def home_page(request):
    return render(request,"core/home_page.html")

def car_view(request):
    return render(request, "car_view\car_view.html")