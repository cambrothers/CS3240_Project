from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.dispatch import receiver
from .models import Profile, Questionnaire, DiscussionThread
from .forms import UserUpdateForm , UserProfileUpdateForm, QuestionnaireForm
from django.views.generic import ListView, DetailView,CreateView
from django.contrib.auth.models import User
from django.db.models import Q

class DiscussionView(ListView):
    model = DiscussionThread
    template_name = 'users/discussion_board.html'
class DiscussionDetail(DetailView):
    model = DiscussionThread
    template_name = 'users/discussion_board_detail.html'
class DiscussionCreate(CreateView):
    model =DiscussionThread
    fields = ['title','description']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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





def matchesList(request):
    from .models import matching_set #, find_best_match
    
    #Must return a dictionary of users to users.
    user_list = matching_set()
    
    instance=request.user

    myMatches = {}

    #To change to top 3 just do a count and stop at top 3.
    for user in user_list:
        if(user_list[user][0] == instance):
            myMatches[user] = user_list[user]

    #print("User_List")
    #print(user_list)
    print("My matches:")
    print(myMatches)

    #myMatches = sorted(myMatches, key=myMatches.get, reverse = True)
    
    context = {'user_list': myMatches, 'currentUser': instance}
    #context = {'user_list': myMatches}

    print()
    
    #The template will not display the dictionary and it has to be a dictionary.
    #demoDict = {"Alex": "alexMapped", "Bill": "billMapped"}
    
    

    return render(request, 'users/matches.html', context)

    

'''
class MatchesListView(ListView):
    from .models import matching_set #, find_best_match

    model = Profile
    context_object_name = 'profile_list'
    template_name = 'users/matches.html'

    #matches = matching_set(model)
    #top3 = find_best_match(model, matches)

    def get__queryset(self):
        return Profile.objects.all()

'''




class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'users/profileDetail.html'


    def get_object(self, queryset=None):
        return get_object_or_404(Profile, pk=self.kwargs.get('pk'))


   

'''
    def get_queryset(self):
        return Profile.objects.all()

'''

