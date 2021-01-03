from .models import Project
# Create your views here.

from .forms import ContactForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.urls import reverse


def home(request):
    return render(request, 'portfolio/home.html')


def about(request):
    return render(request, 'portfolio/about.html')


def success(request):
    return render(request, 'portfolio/success.html')


def contact(request):
    form_class = ContactForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['full_name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email_address']
            message = form.cleaned_data['message']

            message = name + " with email, " + from_email + " , sent the following message:\n\n" + message
            send_mail(subject, message, from_email, ['ooakhu@gmail.com'])
            return HttpResponseRedirect(reverse('portfolio:success'))
    return render(request, 'portfolio/contact.html', {'form': form})


def projects(request):
    # my_projects = Project.objects.all().order_by('name')
    return render(request, 'portfolio/project.html')


