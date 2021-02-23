from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from .homeforms import NewsLetterForm
from django.contrib import messages

# Create your views here.
def landing_page(request):
    return render(request, 'index.html')

def tutorial(request):
    return render(request, 'landing_page/tutorial.html')

def privacy(request):
    return render(request, 'landing_page/privacypolicy.html')

def terms(request):
    return render(request, 'landing_page/terms.html')

def product(request):

    return render(request, 'landing_page/product.html')

def HomePage(request):
    form = NewsLetterForm(request.POST or None)

    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your request! We will get you notify by email soon.')
            return redirect('home')
        else:
            return redirect('home')
    context = {'newsform':form}
    return render(request, 'index.html', context)

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
    
    #send email
        send_mail(
            message_email,
            message,
            message_email,
            ['eddies.startup@gmail.com'],
        )

        return render(request, 'landing_page/contact.html',{'message_name':message_name})

    else:
        return render(request, 'landing_page/contact.html')

def newsletter(request):
    form = NewsLetterForm(request.POST or None)

    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated.')
        return redirect('landing_page:contact')
    context = {'newsform':form}
    return render(request, 'landing_page/base.html', context)

def aboutus(request):
    return render(request, 'landing_page/aboutus.html')
