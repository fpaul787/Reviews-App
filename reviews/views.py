from django.shortcuts import render
from .models import Review

# Create your views here.
posts = [
    {
        'author': 'Frantz',
        'title': 'The Miseducation of Lauryn Hill Review',
        'content': "First post content",
        'date_posted': "May 10, 2020"
    },
    {
        'author': 'Frantz',
        'title': 'Reasonable Doubt Review',
        'content': "First post content",
        'date_posted': "May 10, 2020"
    }
]
def home(request):
    data = {
        'name': "Frantz"
    }

    context = {
        'data': data,
        'reviews': Review.objects.all()
    }
    return render(request, 'home.html' ,context)
