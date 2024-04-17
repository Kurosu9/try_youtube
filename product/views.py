from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def soft(request):
    context = {
        'name': 'Portfolio'
    }
    return render(request, 'index.html', context=context)
