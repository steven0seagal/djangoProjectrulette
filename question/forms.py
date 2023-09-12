from django import forms
from .models import Question, Choice, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text', 'is_correct']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Disable is_correct for existing choices
        if self.instance.pk is not None:
            self.fields['is_correct'].disabled = True

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['choice']

    def __init__(self, question, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['choice'].queryset = question.choice_set.all()
