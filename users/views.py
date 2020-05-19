from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username}')
            return redirect('reviews-home')
    else:
        form = UserRegisterForm()

    formObject = {
        'form': form
    }

    return render(request, 'users/register.html', formObject)

@login_required
def profile(request):
    return render(request, 'users/profile.html')
