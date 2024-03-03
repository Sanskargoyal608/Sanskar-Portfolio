# portfolio/models.py
from django.db import models


topic_choice = (
    ('Project', 'Project'),
    ('Blog', 'Blog'),
    ('UI/UX Project', 'UI/UX Project'),
    ('Certificate', 'Certificate'),
    ('Skills', 'Skills'),
    ('UnityProject', 'UnityProject'),
    ('AppProject', 'AppProject'),

)   


class Upload_Form(models.Model):
    tittle = models.CharField(max_length=200,)
    topic =  models.CharField(max_length=100, choices= topic_choice)
    image = models.URLField()
    intro = models.TextField()
    content = models.TextField()
    skills = models.TextField()
    collab_Mail = models.TextField()
    certifiedBy = models.TextField()

    def __str__(self):
        return self.tittle
    

class ContactUs_Form(models.Model):
    Name = models.CharField(max_length=200,)
    Email =  models.EmailField()
    PhoneNumber = models.IntegerField()
    Topic = models.TextField()
    Message = models.TextField()

    def __str__(self):
        return self.Name   


 