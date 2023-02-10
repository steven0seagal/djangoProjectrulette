from rest_framework import viewsets
from .models import Question, Choice,Answer
from .serializers import QuestionSerializer, ChoiceSerializer,AnswerSerializer
from rest_framework import generics

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class AnswerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class AnswerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer