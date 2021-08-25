from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    context = {
        'name': 'flip'
    }
    return render(request, 'hello.html', context)