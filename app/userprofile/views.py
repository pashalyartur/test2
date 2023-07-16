
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from userprofile.forms import SignupForm
from .models import Userprofile


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/log-in/')
    else:
        form = SignupForm()

    return render(request, 'userprofile/signup.html', {
        'form': form
    })
