from django.shortcuts import render


# Create your views here.

def home(request):
    data = {
        'name': "Frantz"
    }

    context = {
        'data': data
    }
    return render(request, 'reviews/base.html' ,context)
