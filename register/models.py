from django.db import models

# Create your models here.
class Team(models.Model):

    team_name = models.CharField(max_length=255)
    team_number = models.IntegerField()
    person1_name = models.CharField(max_length=255,blank=True,null=True)
    person2_name = models.CharField(max_length=255,blank=True,null=True)
    person3_name = models.CharField(max_length=255,blank=True,null=True)
    person4_name = models.CharField(max_length=255,blank=True,null=True)
    person5_name = models.CharField(max_length=255,blank=True,null=True)
    person6_name = models.CharField(max_length=255,blank=True,null=True)
    person7_name = models.CharField(max_length=255,blank=True,null=True)
    person8_name = models.CharField(max_length=255,blank=True,null=True)
    person9_name = models.CharField(max_length=255,blank=True,null=True)
    person10_name = models.CharField(max_length=255,blank=True,null=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.team_name