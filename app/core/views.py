from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def role(request):
    return render(request,'userprofile/role.html')

def about(request):
    return render(request,'core/about.html')