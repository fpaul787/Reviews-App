from django.shortcuts import render


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
        'posts': posts
    }
    return render(request, 'reviews/home.html' ,context)
