from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from userprofile.forms import SignupForm

from .models import Userprofile
from django.contrib.auth.models import User, Group



#def signup(request):
#    if request.method == 'POST':
#        form = UserCreationForm(request.POST)
#
#        if form.is_valid():
#            user = form.save()
 #           
#
 #           user.members.add(request.user)
  #          user.save()

#            return redirect('/log-in/')
 #   else:
  #      form = SignupForm()

  #  return render(request, 'userprofile/signup.html', {
  #      'form': form
  #  })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            userprofile = Userprofile.objects.create(user=user)
            user.save()

            return redirect('/signup/')

    else:
        form = SignupForm()

    return render(request,'userprofile/signup.html',{
        'form': form 
    })