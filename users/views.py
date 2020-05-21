from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, UserProfileUpdateFrom
from django.contrib import messages

def register(request):
    # can't go to the register page if
    # you're already logged in.
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()

    formObject = {
            'form': form
    }

    return render(request, 'users/register.html', formObject)

@login_required
def profile(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        user_profile_update_form = UserProfileUpdateFrom(request.POST, request.FILES, instance=request.user.profile)

        if user_update_form.is_valid() and user_profile_update_form.is_valid():
            user_update_form.save()
            user_profile_update_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        user_profile_update_form = UserProfileUpdateFrom(instance=request.user.profile)

    context = {
        'u_form': user_update_form,
        'p_form': user_profile_update_form
    }

    return render(request, 'users/profile.html', context)
