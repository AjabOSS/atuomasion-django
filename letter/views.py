from django.shortcuts import render
from .models import Letter

def home_view(request):
    letter = Letter.objects.all()
    context = {
        "letter" : letter
    }
    return render(request, "home.html", context)