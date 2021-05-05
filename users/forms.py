from django import forms
from django.contrib.auth.models import User
from .models import DiscussionThread, Profile , Questionnaire
'''
Title:Django form - set label
Author: Xbito
Date: March 12, 2009
Code Version: n/a
URL: https://stackoverflow.com/questions/636905/django-form-set-label 
Software License: n/a
** used this to see how to set labels to our forms**

Title: Django Tutorials Playlist
Author: Corey Schafer
Date: March 6 , 2018
Code version: n/a
URL: https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p 
Software License: n/a
** used the tutorial to understand how forms work, then built other forms for other models in the project**
'''

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class UserProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image','name','bio','pronouns','age','year','dorm_pref','school','roomates', 'schedule_image','phone_number','insta_handle','twitter_handle','linked_in']
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
            'phone_number': 'Phone Number:',
            'insta_handle': 'Instagram:',
            'twitter_handle': 'Twitter:',
            'linked_in': 'LinkedIn:',
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
            'overnight': 'Are you okay with having overnight guests?',
            'nightlife': 'Do you like to go out to the nightlife scene?',
            'study': 'Do you prefer studying in quiet or loud places?',
            'where': 'Would you like to live on- or off-Grounds?',
            'personality': 'Are you more introverted or extroverted?',
            'sharing': 'Would you be okay with sharing items with your roommates?',
            'gender': 'Would you be okay with roomming with somebody of another gender?',
            'year': 'Do you only want roommates that are the same year as you?'
        }
'''
Title: Create a Simple Django Blog
Author: Codemy.com
Date: Aug 27,2020
Code Version: n/a
URL: https://www.youtube.com/watch?v=J7xaESAddDQ
Software License:n/a
** watched part of this series to understand how we can use forms to create new objects of models. **

'''

class DiscussionForm(forms.ModelForm):
    class Meta:
        model = DiscussionThread
        fields = ['title','description']
#Juliette - added forms for sending friend request and accepting/denying
'''

Title: ChoiceField – Django Forms
Author: NaveenArora
Date: February 13 , 2020
Code Version: n/a
URL: https://www.geeksforgeeks.org/choicefield-django-forms/ 
Software License: n/a

**referenced this tutorial to be able to make forms to friend request/ accept users

Title:How to append elements in Python tuple?
Author: Malhar Lathkar
Date: January 15,2018
Code Version: n/a
URL: https://www.tutorialspoint.com/How-to-append-elements-in-Python-tuple#:~:text=First%2C%20convert%20tuple%20to%20list,list%20object%20back%20to%20tuple.&text=You%20can%20see%20new%20element%20appended%20to%20original%20tuple%20representation. 
Software License: n/a
** also referenced this to see how to append tuples in python


'''
class RequestFriendForm(forms.Form):
    CHOICES = ()
 
    for user in User.objects.all():
        if not user.is_superuser:
            LIST_CHOICES = list(CHOICES)
            LIST_CHOICES.append((user,user))
            CHOICES = tuple(LIST_CHOICES)
    user_to_add = forms.ChoiceField(choices = CHOICES)

class AcceptDenyForm(forms.Form):
    CHOICES = ()
    DECISION = (('ACCEPT','ACCEPT'),('DECLINE','DECLINE'))
    for user in User.objects.all():
        #if not user.is_superuser:
            LIST_CHOICES = list(CHOICES)
            LIST_CHOICES.append((user,user))
            CHOICES = tuple(LIST_CHOICES)
    user_to_add = forms.ChoiceField(choices = CHOICES)
    answer = forms.ChoiceField(choices = DECISION)
