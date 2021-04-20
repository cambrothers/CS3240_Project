from django import forms
from django.contrib.auth.models import User
from .models import Profile , Questionnaire


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
        # Josh - 4/19/21 - Added labels for the questionnaire
        # source: https://stackoverflow.com/questions/36905060/how-can-i-change-the-modelform-label-and-give-it-a-custom-name
        labels = {
            'username': 'Enter a username:',
            'email': 'What\'s your email?'
        }

class UserProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image','name','bio','pronouns','age','year','dorm_pref','school','roomates', 'schedule_image']
        # Josh - 4/19/21 - Added labels for the questionnaire
        # source: https://stackoverflow.com/questions/36905060/how-can-i-change-the-modelform-label-and-give-it-a-custom-name
        labels = {
            'image': 'Upload an image of yourself:',
            'name': 'What\'s your name?',
            'bio': 'Tell us about yourself:',
            'pronouns': 'What are your pronouns?',
            'age': 'How old are you?',
            'year': 'What year are you?',
            'dorm_pref': 'What style dorm do you prefer?',
            'school': 'Which UVA school do you attend?',
            'roomates': 'How many roommates would you like?',
            'schedule_image': 'Upload an image of your schedule',
        }
#Juliette - 4.8.2021 - Made the form for the questionnaire.
class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = ['number_of_roomates','dorm_pref','time_of_day','tidiness','smoke_drink','overnight','nightlife','study','where','personality','sharing','gender','year']
        # Josh - 4/19/21 - Added labels for the questionnaire
        # source: https://stackoverflow.com/questions/36905060/how-can-i-change-the-modelform-label-and-give-it-a-custom-name
        labels = {
            'number_of_roomates': 'How many roommates do you want?',
            'dorm_pref': 'What style dorm would you like to live in?',
            'time_of_day': 'Are you a morning or night person?', 
            'tidiness': 'Are you a clean or messy roommate?',
            'smoke_drink': 'Do you smoke or drink?',
            'overnight': 'Would you allow for overnight guests?',
            'nightlife': 'Do you like to go out to the nightlife scene?',
            'study': 'Do you prefer studying in quiet or loud places?',
            'where': 'Would you like to live on- or off-Grounds?',
            'personality': 'Are you more introverted or extroverted?',
            'sharing': 'Do you mind sharing items with your roommates?',
            'gender': 'Would you be okay with roomming with somebody of another gender?',
            'year': 'Would you be okay with roomming with people outside of your year?'
        }
