from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Ensure that only one choice can be marked as correct
        if self.is_correct:
            Choice.objects.filter(question=self.question).update(is_correct=False)
        super().save(*args, **kwargs)