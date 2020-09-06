from django.shortcuts import render

def home(request):
    """
    Home page
    """
    return render(request, "AdrianMoralesApp/home.html")


def contact(request):
    """
    Contact form
    """
    return render(request, "AdrianMoralesApp/contact.html")
