from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.dispatch import receiver
from .models import Profile, Questionnaire
from .forms import UserUpdateForm , UserProfileUpdateForm, QuestionnaireForm
# Create your views here.
@login_required
def profile(request):
   if hasattr(request.user,'profile'):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST ,instance=request.user)
        up_form = UserProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and up_form.is_valid():
            u_form.save()
            up_form.save()
            messages.success(request,f'Your account has successfully been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        up_form = UserProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form' : u_form,
        'up_form': up_form
    }
    return render(request,'users/profile.html',context) 
   else:
      instance = request.user
      Profile.objects.create(user=instance)
      if request.method == 'POST':
            u_form = UserUpdateForm(request.POST ,instance=request.user)
            up_form = UserProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
            if u_form.is_valid() and up_form.is_valid():
                u_form.save()
                up_form.save()
                messages.success(request,f'Your account has successfully been updated!')
                return redirect('profile')
      else:
            u_form = UserUpdateForm(instance=request.user)
            up_form = UserProfileUpdateForm(instance=request.user.profile)
      context = {
            'u_form' : u_form,
            'up_form': up_form
        }
      return render(request,'users/profile.html',context) 
    #Juliette - 4.8.2021 - adding new view for the questionnaire
@login_required
def questionnaire(request):
   if hasattr(request.user,'questionnaire'):
    if request.method == 'POST':
        q_form = QuestionnaireForm(request.POST,instance=request.user.questionnaire)
        if q_form.is_valid():
            q_form.save()
            return redirect('questionnaire')
    else:
             q_form = QuestionnaireForm(request.POST ,instance=request.user.questionnaire)
             context = {
            'q_form' : q_form,
            
        }
             return render(request,'users/questionnaire.html',context) 
   else:
       instance = request.user
       Questionnaire.objects.create(user=instance)
       if request.method == 'POST':
            q_form = QuestionnaireForm(request.POST ,instance=request.user.questionnaire)
            if q_form.is_valid():
               q_form.save()
               return redirect('questionnaire')
       else:
             q_form = QuestionnaireForm(request.POST ,instance=request.user.questionnaire)
             context = {
            'q_form' : q_form,
            
        }
             return render(request,'users/questionnaire.html',context)    
