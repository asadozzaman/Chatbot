from django.shortcuts import render

# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')

def chatui(request):
    return render(request, 'chatui.html')

def pricing(request):
    return render(request, 'pricing.html')


def faq(request):
    return render(request, 'faq.html')

def profile(request):
    return render(request, 'profile.html')