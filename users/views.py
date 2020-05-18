from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form = UserCreationForm()

    formObject = {
        'form': form
    }

    return render(request, 'users/register.html', formObject)
