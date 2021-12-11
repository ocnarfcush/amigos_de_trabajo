from django.db import models
from django.db.models.base import Model
from django.db.models.fields import TextField
from django.urls import reverse
from django.contrib.auth.models import User
from .locals import LOCALITIES
import string
import random


class AddInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    whatsappid = models.CharField(max_length=50, null=True, blank=True)
    facebookid = models.CharField(max_length=50, null=True, blank=True)
    instagramid = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.user.username


class Forum(models.Model):
    area = models.CharField(max_length=50, choices=LOCALITIES)
    title = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.RESTRICT)
    creation_time = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


class ForumMessage(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.RESTRICT)
    message = models.TextField(max_length=500)
    message_owner = models.ForeignKey(User, on_delete=models.RESTRICT)
    post_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message_owner.username


class Chat(models.Model):
    area = models.CharField(max_length=50, choices=LOCALITIES)
    def __str__(self):
        return self.area


class ChatMessage(models.Model):
    chatroom = models.ForeignKey(Chat, on_delete=models.RESTRICT)
    message = models.TextField(max_length=500)
    message_owner = models.ForeignKey(User, on_delete=models.RESTRICT)
    post_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message_owner.username


class LegalForm(models.Model):
    type = models.CharField(max_length=100)
    file = models.FileField(upload_to='legal_forms/')
    def __str__(self):
        return self.type


class Employer(models.Model):
    name = models.CharField(max_length=100)
    area = models.CharField(max_length=50, choices=LOCALITIES)
    rating = models.FloatField(null=True, blank=True)
    def __str__(self):
        return self.name


class EmployerComment(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.RESTRICT)
    comment = models.TextField(max_length=500)
    comment_owner = models.ForeignKey(User, on_delete=models.RESTRICT)
    post_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_owner.username


class EmploymentOppurtunity(models.Model):
    area = models.CharField(max_length=50, choices=LOCALITIES)
    contact_person = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_number = models.IntegerField()
    active = models.BooleanField(default=True)
    employer = models.CharField(max_length=50)
    stop_recruitment = models.DateField()
    def __str__(self):
        return self.area


class ImmigrationHelpdesk(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.applicant.username


class LearnEnglish(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=100)
    def __str__(self):
        return self.applicant.username


class SpanishBusiness(models.Model):
    area = models.CharField(max_length=50, choices=LOCALITIES)
    businessname = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.businessname




'''
advertisers, legal, education, radio station, banners(small ad)
list resources -- job for angel
scrape resources (locations from maps)
'''