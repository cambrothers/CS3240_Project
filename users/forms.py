from django import forms
from django.contrib.auth.models import User
from .models import DiscussionThread, Profile , Questionnaire


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class UserProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image','name','bio','pronouns','age','year','dorm_pref','school','roomates', 'schedule_image','phone_number','insta_handle','twitter_handle','linked_in']
#Juliette - 4.8.2021 - Made the form for the questionnaire.
class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = ['number_of_roomates','dorm_pref','time_of_day','tidiness','smoke_drink','overnight','nightlife','study','where','personality','sharing','gender','year']

class DiscussionForm(forms.ModelForm):
    class Meta:
        model = DiscussionThread
        fields = ['title','description']