from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'base/index.html')


def about(request):
    return render(request, 'base/about.html')


def welcome(request):
    return render(request, 'base/welcome.html')


def survey(request):
    return render(request, 'base/survey.html')
