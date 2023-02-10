from rest_framework import serializers
from .models import Question, Choice,Answer

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'question', 'choice_text', 'is_correct')


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date', 'choices')



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

