from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Team
def register(request):
    return render(request, 'quiz/register.html')

def create_account(request):
    print(request.POST)
    # team_name = request.GET['team_name']
    # team_number = request.POST['team_number']
    # person1_name = request.POST['person1_name']
    # person2_name = request.POST['person2_name']
    # person3_name = request.POST['person3_name']
    # person4_name = request.POST['person4_name']
    # person5_name = request.POST['person5_name']
    # person6_name = request.POST['person6_name']
    # person7_name = request.POST['person7_name']
    # person8_name = request.POST['person8_name']
    # person9_name = request.POST['person9_name']
    # person10_name = request.POST['person10_name']
    # team = Team(team_name=team_name, team_number=team_number, person1_name=person1_name, person2_name=person2_name,
    #             person3_name=person3_name, person4_name=person4_name, person5_name=person5_name,
    #             person6_name=person6_name, person7_name=person7_name, person8_name=person8_name,
    #             person9_name=person9_name, person10_name=person10_name)
    # team.save()
    return render(request, 'quiz/single_question.html')