from django.shortcuts import render, redirect, reverse
from .forms import forfileform
from .models import forfile
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from accounts.userforms import UserProfileForm
from accounts.models import UserProfile
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.db import models

# Create your views here.
@login_required(login_url='/accounts/login/')
def dashboard(request):
    return render(request, 'dashboard/home.html')

@login_required(login_url='/accounts/login/')
def profile(request, pk):
    files = forfile.objects.filter(user=request.user)

    return render(request, 'dashboard/profile.html')
        
@login_required(login_url='/accounts/login/')
def edit_profile(request, pk):
    user = request.user.userprofile
    form = UserProfileForm(instance=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user,)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
        return redirect('dashboard:profile',pk=pk)
    context = {'editform':form}
    return render(request, 'dashboard/editprofile.html', context)

def overview(request):
    return render(request, 'dashboard/overview.html')

def preprocessing(request):
    return render(request, 'dashboard/preprocessing.html')

def processing(request):
    return render(request, 'dashboard/processing.html')

def visualization(request):
    return render(request, 'dashboard/visualization.html')

def validation(request):
    return render(request, 'dashboard/validation.html')


