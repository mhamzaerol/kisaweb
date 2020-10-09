from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe

from tinymce.models import HTMLField

# Create your models here.

ELECTION_MEDIA_UPLOAD_URL = 'election/img'

class Candidate(models.Model):
    name = models.CharField(max_length=100, default='')
    manifesto = HTMLField()
    speech_url = models.CharField(max_length=512, blank=True, null=True)
    kisa_history = HTMLField()
    image = models.ImageField(upload_to=ELECTION_MEDIA_UPLOAD_URL, blank=True, null=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        if not self.image:
            path = '/static/img/candidate-default-dist.png'
        else:
            path = self.image.url
        return mark_safe(f'<img src="{path}" alt="Candidate Image" width="200" height="200" />')


class Election(models.Model):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    candidates = models.ManyToManyField(Candidate, blank=False)
    intro_msg = HTMLField()
    instructions = HTMLField()
    image = models.ImageField(upload_to=ELECTION_MEDIA_UPLOAD_URL, blank=True, null=True)

    def __str__(self):
        month = int(self.start_datetime.strftime('%-m'))
        year = self.start_datetime.strftime('%Y')
        if month < 8:
            semester = 'Spring'
        else:
            semester = 'Fall'
        return f'{semester} {year}'

    def image_tag(self):
        if not self.image:
            path = '/static/img/election-default-dist.png'
        else:
            path = self.image.url
        return mark_safe(f'<img src="{path}" alt="Election Image" width="150px" height="150px" />')