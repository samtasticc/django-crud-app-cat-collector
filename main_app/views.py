from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')
    # return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')