from django.shortcuts import render
from . forms import *
from django.contrib import messages
from django.views import generic
import requests
from django.core.mail import send_mail
from django.conf import settings


def base(request):
    return render(request, 'base.html')


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact(
                message_about=request.POST['message_about'],
                name=request.POST['name'],
                email=request.POST['email'],
                subject=request.POST['subject'],
                message=request.POST['message']
            )
            contact.save()
            messages.success(request, 'Your Message has been send successfully. We will get back to you soon Via Email.')

            # Define the message variable
            message = f"From: {contact.name}, Email: {contact.email}, Subject: {contact.subject}, Message: {contact.message}"

            # Send the email to multiple recipients
            recipients = ['wield627@gmail.com']
            send_mail(contact.subject, message, 'settings.EMAIL_HOST_USER', recipients, fail_silently=False)
    else:
        form = ContactForm
    context = {
        'form': form,
    }
    return render(request, 'pages/contact.html', context)


def members(request):
    return render(request, 'pages/members.html')


# from django.core.mail import send_mail

def join(request):
    if request.method == 'POST':
        form = MembersForm(request.POST)
        if form.is_valid():
            member = form.save(commit=True)
            member.person_with_disability = form.cleaned_data['person_with_disability']
            member.save()
            messages.success(request, f"Check your email We Have send a confirmation email")
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            subject = "Welcome to our community"
            message = f"Dear {first_name} {last_name}, Thank you for joining our community! We are happy to have you with us."
            email_from = "wield627@gmail.com"
            recipient_list = [form.cleaned_data['email'], ]
            send_mail(subject, message, email_from, recipient_list)

    else:
        form = MembersForm
    context = {
        'form': form,
    }
    return render(request, 'auth/join.html', context)
