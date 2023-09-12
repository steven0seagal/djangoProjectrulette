from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('question', views.create_account, name='create_account'),
    path('question_2', views.create_account, name='question2'),
    path('question_3', views.create_account, name='question3'),
]