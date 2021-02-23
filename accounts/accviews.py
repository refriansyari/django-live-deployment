from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from .models import UserProfile
from . import userforms
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .userforms import UserSignUpForm, UserAccountForm
from django.contrib.auth.decorators import login_required
# Create your views here.

class SignUp(SuccessMessageMixin, CreateView):
    form_class = userforms.UserSignUpForm
    template_name = 'accounts/signup.html'
    success_message = 'Thank you for your registration. Please check your email to verify your account.'
    success_url = reverse_lazy('login')

@login_required(login_url='/accounts/login/')
def personal(request,pk):
    if UserProfile.objects.filter(user=request.user).exists():
        return redirect('dashboard:profile', pk=pk)
    else:
        if request.method == 'POST':
            form = userforms.UserProfileForm(request.POST, request.FILES)
            if form.is_valid():
                files = form.save(commit=False) 
                files.user = request.user
                files.save()
            return redirect('dashboard:profile', pk=pk)

        else:
            form = userforms.UserProfileForm()

    return render(request, 'accounts/personal.html',{
        'userform': form,
    })

@login_required(login_url='/accounts/login/')
def edit_account(request, pk):
    user = request.user
    form = UserAccountForm(instance=user)

    if request.method == 'POST':
        form = UserAccountForm(request.POST, instance=user,)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated.')
        return redirect('dashboard:profile', pk=pk)
    context = {'editform':form}
    return render(request, 'accounts/updateaccounts.html', context)
