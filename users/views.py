from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.dispatch import receiver
from .models import Profile, Questionnaire, DiscussionThread
from .forms import AcceptDenyForm, RequestFriendForm, UserUpdateForm , UserProfileUpdateForm, QuestionnaireForm
from django.views.generic import ListView, DetailView,CreateView
from django.contrib.auth.models import User
from django.db.models import Q
#import request
import cgi
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
#Juliette - added views for friends and friend requests
def friends(request):

    a_p = Profile.objects.all()
    fr_form = RequestFriendForm(request.POST or None)
    context = {
        'all_profiles' :a_p,
        'fr_form':fr_form,
         #'data':data

    }
    if fr_form.is_valid():
        
        data = fr_form.cleaned_data["user_to_add"]
        p = Profile.objects.get(user=request.user)
        print("P is: "+str(p))
        d = User.objects.get(username=data)
        #p.add_request(d)
        d.profile.add_request(request.user)
        print(p.requests)
        print(d.profile.requests.all())
        #context['data'] = data
        print(data)
    return render(request, 'users/friends.html', context)

   
def friend_req(request):
   
    a_p = Profile.objects.all()
    dec_form = AcceptDenyForm(request.POST or None)
    context = {
        'all_profiles' :a_p,
        'dec_form':dec_form,
         #'data':data

    }
    if dec_form.is_valid():
        
        u = dec_form.cleaned_data["user_to_add"]
        a = dec_form.cleaned_data["answer"]
        p = Profile.objects.get(user=request.user)
        print("P is: "+str(p))
       
        
        d = User.objects.get(username=u)
        print("D is: "+str(d))
        #print(d.profile.requests.all())
        if a == 'ACCEPT':
            if d != None :
                print(str(d.profile.requests.all()))
                p.friends.add(d)
                print("Friend added: "+str(p.friends.all()))
                p.requests.remove(d)
                d.profile.friends.add(p.user)
                print(d.profile.get_friends())
            #d.profile.requests.remove(request.user)
            #context['data'] = u
            print(u)
    return render(request, 'users/friend_requests.html', context)
   
class FriendCreate(CreateView):
    model =Profile
    fields = ['name','requests']
    def form_valid(self,form):
        form.instance.user = self.request.user
        return redirect('friend_req')
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
    print("user_list:")
    print(user_list)
    instance=request.user

    my_matches = {}

    #To change to top 3 just do a count and stop at top 3.
    for user, user_l in user_list.items():
        print(user)
        for u in user_l:
            if(u[0] == instance):
             my_matches[user] = u[1]

    #print("User_List")
    #print(user_list)
    print("My matches:")
    print(my_matches)

    my_matches = dict(sorted(my_matches.items(), key=lambda item: item[1], reverse = True))
    print(my_matches)

   # print(type(my_matches))
    context = {'matches': my_matches, 'currentUser': instance}
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
