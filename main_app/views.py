from django.shortcuts import render
from django.http import HttpResponse

class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name,
        self.breed = breed,
        self.description = description,
        self.age = age
        
cats = [
    Cat('Lolo', 'tabby', 'Kinda rude.', 3),
    Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
    Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
    Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

def home(request):
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')
    # return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

    def cat_index(request):
        return render(request, 'cats/index.html', {'cats': cats})