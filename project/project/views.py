from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    subject="leave for a rakhi "
    message="3days leave "
    from_email="badkursiddharth282@gmail.com"
    user=["patelmehak2003@gmail.com"]
    send_mail(subject,message,from_email,user)
    return HttpResponse("done message")