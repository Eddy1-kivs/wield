from django import forms
from django.forms import widgets
from .models import *
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'


class MembersForm(forms.ModelForm):
    class Meta:
        model = Members
        person_with_disability = forms.BooleanField(required=False)
        widgets = {'date_of_birth': DateInput()}
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'preferred_language',
                  'gender',
                  'pronoun', 'person_with_disability']

    def clean(self):
        cleaned_data = super().clean()
        dob = cleaned_data.get("date_of_birth")
        age = datetime.date.today().year - dob.year - ((datetime.date.today().month, datetime.date.today().day) < (dob.month, dob.day))
        cleaned_data['age'] = age
        self.instance.age = age


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['message_about', 'name', 'email', 'subject', 'message']


