from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class UserProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['name','bio','pronouns','age','year','dorm_pref','school','roomates', 'schedule_image']