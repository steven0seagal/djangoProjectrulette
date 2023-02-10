from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def question(request):
    return render(request, 'quiz/single_question.html')

