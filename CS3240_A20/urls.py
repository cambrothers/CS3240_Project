"""CS3240_A20 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from users import views as users_views
from django.conf import settings 
from django.conf.urls.static import static
from users.views import ProfileDetailView, DiscussionView ,matchesList,DiscussionDetail ,DiscussionCreate#, MatchesListView,

urlpatterns = [
    path('', TemplateView.as_view(template_name='CS3240_A20/index.html'),name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('profile/', users_views.profile, name='profile'),
    # Juliette - 4.8.2021 - New Views
    path('questionnaire/', users_views.questionnaire, name='questionnaire'),
    path('questionnaire_done/', TemplateView.as_view(template_name='users/questionnaire_done.html'),name='qd'),
    
    path('profile/matches/', matchesList, name='matches'),  
    path('profile/matches/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('discussions/' , DiscussionView.as_view() ,name="discussions"),
    path('discussions/<int:pk>/', DiscussionDetail.as_view(),name='discussions_detail'),
    path('discussions/new/', DiscussionCreate.as_view(),name='discussions_create')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    #Testing pushing change to remote repo