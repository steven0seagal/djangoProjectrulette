from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def mainsite(request):
    return render(request, 'mainsite/main.html')

