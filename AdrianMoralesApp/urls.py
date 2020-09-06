from django.urls import path
from AdrianMoralesApp import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('contact', views.contact, name="Contact"),
]
