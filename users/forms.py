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
#Juliette - added forms for sending friend request and accepting/denying
class RequestFriendForm(forms.Form):
    CHOICES = ()
 
    for user in User.objects.all():
       # if not user.is_superuser:
            LIST_CHOICES = list(CHOICES)
            LIST_CHOICES.append((user,user))
            CHOICES = tuple(LIST_CHOICES)
    user_to_add = forms.ChoiceField(choices = CHOICES)

class AcceptDenyForm(forms.Form):
    CHOICES = ()
    DECISION = (('ACCEPT','ACCEPT'),('DECLINE','DECLINE'))
    for user in User.objects.all():
     #   if not user.is_superuser:
            LIST_CHOICES = list(CHOICES)
            LIST_CHOICES.append((user,user))
            CHOICES = tuple(LIST_CHOICES)
    user_to_add = forms.ChoiceField(choices = CHOICES)
    answer = forms.ChoiceField(choices = DECISION)