from django.urls import path
from core import views

app_name= 'core_url'
urlpatterns = [
    path('',views.index )
]
