from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime, timedelta

# Create your models here.


class Members(models.Model):
    gender = (('Female', 'female'), ('Transgender', 'Transgender'), ('Prefer Not to identify', 'Prefer Not to identify')
              , ('Male', 'Male'))
    preferred_language = (('English', 'English'), ('Kiswahili', 'Kiswahili'))
    pronouns = (('She/her', 'She/her'), ('He', 'Him'), ('Prefer Not to say', 'Prefer Not to say'))

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField(null=True)
    age = models.IntegerField()
    preferred_language = models.CharField(choices=preferred_language, null=True, max_length=100)
    gender = models.CharField(choices=gender, null=True, max_length=100)
    pronoun = models.CharField(choices=pronouns, null=True, max_length=100)
    person_with_disability = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.first_name


class Contact(models.Model):
    about = (('membership', 'membership'), ('privacy policy clarification', 'privacy policy clarification'),
             ('other', 'other'))

    message_about = models.CharField(choices=about, null=True, max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.message_about


