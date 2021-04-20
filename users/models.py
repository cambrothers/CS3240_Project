from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from CS3240_A20 import settings
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
#May need to pip install django-imagekit if import statements aren't working. Note imagekit depends on Pillow.
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, SmartResize
from PIL import Image
from django.db.models import Q
from datetime import datetime    
# Create your models here.
User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False



#Assign each user a number of points against every other user then 




class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    friends = models.ManyToManyField(User,related_name="friends",blank=True)
    requests = models.ManyToManyField(User,related_name="requests",blank=True)

    phone_number = models.CharField(max_length=10,blank=True,default="")
    insta_handle = models.CharField(max_length=300,blank=True,default="")
    twitter_handle = models.CharField(max_length=300,blank=True,default="")
    linked_in = models.CharField(max_length=300,blank=True,default="")

    #questionaire = models.OneToOneField(Questionnaire, on_delete=models.CASCADE)

    image = models.ImageField( upload_to="images/", default="media/images/noimage_rb51dj.png")
    name = models.CharField(max_length=400)
    bio = models.CharField(max_length=500,blank=True,default="")
    pronouns = models.CharField(max_length=400,blank=True,default="")
    age = models.PositiveIntegerField(default=17,blank=True)
    year = models.PositiveIntegerField(default=1,blank=True)

    schedule_image = models.ImageField( upload_to="images/",default="media/images/noschedule_zdconk.png")
    
    #matches = matching_set(self)
    #top3 = find_best_match(self, matches)
   # thumbnail = ImageSpecField(source='schedule_image', processors=[ResizeToFill(1000,500)], format='PNG')

    class DormChoice(models.TextChoices):
        NONE = "No preference."
        HALL = "Hall-Style"
        SUITE = "Suite-Style"
    dorm_pref = models.CharField(max_length= 100,choices=DormChoice.choices,default=DormChoice.NONE,blank=True)
    class SchoolChoice(models.TextChoices):
        DEFAULT = "default"
        COLLEGE = "College and Graduate School of Arts and Sciences"
        ENGINEERING = "School of Engineering and Applied Science"
        ARCHITECTURE = "School of Architecture"
        COMMERCE = "McIntire School of Commerce"
        NURSING = "School of Nursing"
        MED = "School of Medicine"
        LAW = "School of Law"
        EDUCATION = "School of Education and Human Development"
        DATA_SCIENCE =  "School of Data Science"
        PROFESSIONAL_STUDIES = "School of Continuing & Professional Studies"
        LEADERSHIP = "Frank Batten School of Leadership and Public Policy"
        BUSINESS = "Darden School of Business"
      
    school = models.CharField(max_length= 500,choices=SchoolChoice.choices,default=SchoolChoice.DEFAULT,blank=True)
    roomates = models.PositiveIntegerField(default=0,blank=True)
    def get_friends(self):
        return self.friends.all()
    def get_requests(self):
        return self.requests.all()
    def add_request(self,a):      
        if not a in self.requests.all():
            self.requests.add(a)
    def get_friends_num(self):
        return self.friends.all().count()
    def __str__(self):
        return f'{self.user.username}'


#Juliette - 4.8.2021 - Creating a new model for the questionnaire with fields representing each question
class Questionnaire(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    class RoomatesChoice(models.TextChoices):
        ZERO = "Zero"
        ONE = "One" 
        TWO = "Two"
        THREE ="Three"
        FOUR ="Four"
        FIVE ="Five"
    number_of_roomates = models.CharField(max_length= 100,choices=RoomatesChoice.choices,default=RoomatesChoice.ZERO)
    class DormChoice(models.TextChoices):
        NONE = "No preference."
        HALL = "Hall-Style"
        SUITE = "Suite-Style"
    dorm_pref = models.CharField(max_length= 100,choices=DormChoice.choices,default=DormChoice.NONE)
    class TODChoice(models.TextChoices):
        NEITHER = "Neither a night owl or early bird"
        NIGHT = "I'm a night owl"
        MORNING = "I'm more of a morning person"
    time_of_day = models.CharField(max_length= 100,choices=TODChoice.choices,default=TODChoice.NEITHER)
    class TidinessChoice(models.TextChoices):
        NEITHER = "I'm not overly clean nor messy"
        MESSY= "I'm a more messy person"
        CLEAN = "I'm more of a clean person"
    tidiness = models.CharField(max_length= 100,choices=TidinessChoice.choices,default=TidinessChoice.NEITHER)
    class SmokeDrinkChoice(models.TextChoices):
        NO = "No, I do not"
        YES= "Yes, I do"

     
    smoke_drink = models.CharField(max_length= 100,choices=SmokeDrinkChoice.choices,default=SmokeDrinkChoice.NO)
    class OvernightChoice(models.TextChoices):
        NO = "No, I would not be okay with an overnight guest"
        YES= "Yes, I would be okay with overnight guests"
     
    overnight = models.CharField(max_length= 100,choices=OvernightChoice.choices,default=OvernightChoice.NO)
    class NightlifeChoice(models.TextChoices):
        NO = "No, I do not like going out at night"
        YES= "Yes, I go out at night"
     
    nightlife = models.CharField(max_length= 100,choices=NightlifeChoice.choices,default=NightlifeChoice.NO)
    class StudyChoice(models.TextChoices):
        QUIET = "I prefer a quiet environment while studying"
        LOUD= "I don't mind noise or music while studying"
     
    study = models.CharField(max_length= 100,choices=StudyChoice.choices,default=StudyChoice.QUIET)
    class WhereChoice(models.TextChoices):
        ON_GROUNDS = "I want to live on-grounds"
        OFF_GROUNDS= "I want to live off-grounds"
        NO_PREF = "I have no preference"
    where = models.CharField(max_length= 100,choices=WhereChoice.choices,default=WhereChoice.NO_PREF)
    class PersonalityChoice(models.TextChoices):
        INTROVERT = "I am more introverted"
        EXTROVERT= "I am more extroverted"
       
    personality = models.CharField(max_length= 100,choices= PersonalityChoice.choices,default= PersonalityChoice.INTROVERT)
    class SharingChoice(models.TextChoices):
        YES = "I would be ok to share/borrow things from roommates"
        NO=  "I would not be ok to share/borrow things from roommates"
       
    sharing = models.CharField(max_length= 100,choices= SharingChoice.choices,default= SharingChoice.NO)
    class GenderChoice(models.TextChoices):
        YES = "I would be ok to have roomates of different genders"
        NO=  "I would not be ok to have roomates of different genders"
       
    gender = models.CharField(max_length= 100,choices= GenderChoice.choices,default= GenderChoice.NO)
    class YearChoice(models.TextChoices):
        YES = "I only want to room with people my year"
        NO=  "I don't mind rooming with people of different years"
       
    year = models.CharField(max_length= 100,choices=  YearChoice.choices,default=  YearChoice.NO)
    def __str__(self):
        return f'{self.user}- Questionnaire'
# Juliette - making new model for the discussion threads
class DiscussionThread(models.Model):
    author = models.CharField(max_length=300,default="")
    title = models.CharField(max_length=300,default="")
    description = models.CharField(max_length=500,default="")
    def get_absolute_url(self):
        return reverse('discussions_detail',kwargs={'pk': self.pk})
    def __str__(self):
        return f'{self.author} - Discussion Thread'


 # not working right now, but this is supposed to resize the image when there's a new upload to thr profile_img
    # i think cloudinary has a different method
    #def save(self):
        #super().save()

        #img = Image.open(self.image.path)

        #if img.height > 300 or img.width > 300:
            #output_size = (300, 300)
            #img.thumbnail(output_size)
            #img.save(self.image.path)

            #travis test



#COMMENT HERE TO PUSH












#Campbell Brothers: 4/11 Adding a matching algorithm to the questionnaire

def matching_set():
    
    #Now want to do point algo and must return a dictionary that maps user objects to user objects.
    #See if can take the algo already given and apply it with user objects only not strings.
    
    matches = {}
    user_set = User.objects.all()
    matching_points = 0
    for u in user_set:
        for v in user_set:
            #Roommate choice is based on a ranking. If there is a no difference between the number, ex. [0,0] 
            #then there is 5 points added. If there is one difference: +4; two difference: +3; three 
            #difference: +2, and four/five difference: +1

            #All scores are the same bc the questionaire saves to be the same for all users.
            

            if(u != v) and hasattr(u,"questionnaire") and hasattr(v,"questionnaire"):
              if (not u.is_superuser) and (not v.is_superuser):
                print ("u :"+u.username+" is an admin (True/False): "+ str(u.is_superuser))
                print ("v :"+v.username+" is an admin (True/False): "+ str(v.is_superuser))
                # 4/16/21 - Josh - Slight changes to algorithm
                
                # NUMBER OF ROOMMATES
                # u.questionnaire.number_of_roommates == 5
                if (u.questionnaire.number_of_roomates == "Five") and (v.questionnaire.number_of_roomates == "Five"): #and  (v.questionnaire.RoomatesChoice.FIVE):
                    matching_points = matching_points  + 5
                elif (u.questionnaire.number_of_roomates == "Five") and  (v.questionnaire.number_of_roomates == "Four"):
                    matching_points = matching_points  + 4
                elif (u.questionnaire.number_of_roomates == "Five") and  (v.questionnaire.number_of_roomates == "Three"):
                    matching_points = matching_points  + 3
                elif (u.questionnaire.number_of_roomates == "Five") and  (v.questionnaire.number_of_roomates == "Two"):
                    matching_points = matching_points  + 2
                elif (u.questionnaire.number_of_roomates == "Five") and  (v.questionnaire.number_of_roomates == "One"):
                    matching_points = matching_points  + 1
                elif (u.questionnaire.number_of_roomates == "Five") and  (v.questionnaire.number_of_roomates == "Zero"):
                    matching_points = matching_points  + 1

                # u.questionnaire.number_of_roommates == 4
                elif (u.questionnaire.number_of_roomates == "Four") and  (v.questionnaire.number_of_roomates == "Five"):
                    matching_points = matching_points  + 4
                elif (u.questionnaire.number_of_roomates == "Four") and  (v.questionnaire.number_of_roomates == "Four"):
                    matching_points = matching_points  + 5
                elif (u.questionnaire.number_of_roomates == "Four") and  (v.questionnaire.number_of_roomates == "Three"):
                    matching_points = matching_points  + 4
                elif (u.questionnaire.number_of_roomates == "Four") and  (v.questionnaire.number_of_roomates == "Two"):
                    matching_points = matching_points  + 3
                elif (u.questionnaire.number_of_roomates == "Four") and  (v.questionnaire.number_of_roomates == "One"):
                    matching_points = matching_points  + 2
                elif (u.questionnaire.number_of_roomates == "Four") and  (v.questionnaire.number_of_roomates == "Zero"):
                    matching_points = matching_points  + 1

                # u.questionnaire.number_of_roommates == 3
                elif (u.questionnaire.number_of_roomates == "Three") and  (v.questionnaire.number_of_roomates == "Five"):
                    matching_points = matching_points  + 3
                elif (u.questionnaire.number_of_roomates == "Three") and  (v.questionnaire.number_of_roomates == "Four"):
                    matching_points = matching_points  + 4
                elif (u.questionnaire.number_of_roomates == "Three") and  (v.questionnaire.number_of_roomates == "Three"):
                    matching_points = matching_points  + 5
                elif (u.questionnaire.number_of_roomates == "Three") and  (v.questionnaire.number_of_roomates == "Two"):
                    matching_points = matching_points  + 4
                elif (u.questionnaire.number_of_roomates == "Three") and  (v.questionnaire.number_of_roomates == "One"):
                    matching_points = matching_points  + 3
                elif (u.questionnaire.number_of_roomates == "Three") and  (v.questionnaire.number_of_roomates == "Zero"):
                    matching_points = matching_points  + 2

                # u.questionnaire.number_of_roommates == 2
                elif (u.questionnaire.number_of_roomates == "Two") and  (v.questionnaire.number_of_roomates == "Five"):
                    matching_points = matching_points  + 2
                elif (u.questionnaire.number_of_roomates == "Two") and  (v.questionnaire.number_of_roomates == "Four"):
                    matching_points = matching_points  + 3
                elif (u.questionnaire.number_of_roomates == "Two") and  (v.questionnaire.number_of_roomates == "Three"):
                    matching_points = matching_points  + 4
                elif (u.questionnaire.number_of_roomates == "Two") and  (v.questionnaire.number_of_roomates == "Two"):
                    matching_points = matching_points  + 5
                elif (u.questionnaire.number_of_roomates == "Two") and  (v.questionnaire.number_of_roomates == "One"):
                    matching_points = matching_points  + 4
                elif (u.questionnaire.number_of_roomates == "Two") and  (v.questionnaire.number_of_roomates == "Zero"):
                    matching_points = matching_points  + 3

                # u.questionnaire.number_of_roommates == 1
                elif (u.questionnaire.number_of_roomates == "One") and  (v.questionnaire.number_of_roomates == "Five"):
                    matching_points = matching_points  + 1
                elif (u.questionnaire.number_of_roomates == "One") and  (v.questionnaire.number_of_roomates == "Four"):
                    matching_points = matching_points  + 2
                elif (u.questionnaire.number_of_roomates == "One") and  (v.questionnaire.number_of_roomates == "Three"):
                    matching_points = matching_points  + 3
                elif (u.questionnaire.number_of_roomates == "One") and  (v.questionnaire.number_of_roomates == "Two"):
                    matching_points = matching_points  + 4
                elif (u.questionnaire.number_of_roomates == "One") and  (v.questionnaire.number_of_roomates == "One"):
                    matching_points = matching_points  + 5
                elif (u.questionnaire.number_of_roomates == "One") and  (v.questionnaire.number_of_roomates == "Zero"):
                    matching_points = matching_points  + 4

                # u.questionnaire.number_of_roommates == 0
                elif (u.questionnaire.number_of_roomates == "Zero") and  (v.questionnaire.number_of_roomates == "Five"):
                    matching_points = matching_points  + 1
                elif (u.questionnaire.number_of_roomates == "Zero") and  (v.questionnaire.number_of_roomates == "Four"):
                    matching_points = matching_points  + 1
                elif (u.questionnaire.number_of_roomates == "Zero") and  (v.questionnaire.number_of_roomates == "Three"):
                    matching_points = matching_points  + 2
                elif (u.questionnaire.number_of_roomates == "Zero") and  (v.questionnaire.number_of_roomates == "Two"):
                    matching_points = matching_points  + 3
                elif (u.questionnaire.number_of_roomates == "Zero") and  (v.questionnaire.number_of_roomates == "One"):
                    matching_points = matching_points  + 4
                elif (u.questionnaire.number_of_roomates == "Zero") and  (v.questionnaire.number_of_roomates == "Zero"):
                    matching_points = matching_points  + 5
               
                # DORM PREFERENCE
                # If the same preference, +5. If one doesn't care, +3. If both have different preferences, +1. 
                if (u.questionnaire.dorm_pref == v.questionnaire.dorm_pref):
                    matching_points += 5
                elif (u.questionnaire.dorm_pref == "No preference.") or (v.questionnaire.dorm_pref == "No preference."):
                    matching_points += 3
                else: 
                    matching_points += 1
                
                # SLEEPING HABITS
                # If the same preference, +5. If one doesn't care, +3. If both have different preferences, +1. 
                if (u.questionnaire.time_of_day == v.questionnaire.time_of_day):
                    matching_points += 5
                elif (u.questionnaire.time_of_day == "Neither a night owl or early bird") or (v.questionnaire.time_of_day == "Neither a night owl or early bird"):
                    matching_points += 3
                else:
                    matching_points += 1

                # TIDINESS
                # If both the same, +5. If one is centered, +3. If both are different, +1. 
                if (u.questionnaire.tidiness == v.questionnaire.tidiness):
                    matching_points += 5
                elif (u.questionnaire.tidiness == "I'm not overly clean nor messy") or (v.questionnaire.tidiness == "I'm not overly clean nor messy"):
                    matching_points += 3
                else:
                    matching_points += 1
                
                # SMOKING & DRINKING
                if (u.questionnaire.smoke_drink == v.questionnaire.smoke_drink): #and (v.questionnaire.SmokeDrinkChoice.YES):
                    matching_points = matching_points + 5
                elif (u.questionnaire.smoke_drink != v.questionnaire.smoke_drink): #and (v.questionnaire.SmokeDrinkChoice.YES):
                    matching_points = matching_points + 1

                # OVERNIGHT GUESTS
                if (u.questionnaire.overnight == v.questionnaire.overnight):
                    matching_points = matching_points + 5
                elif (u.questionnaire.overnight != v.questionnaire.overnight):
                    matching_points = matching_points + 1

                # NIGHTLIFE
                if (u.questionnaire.nightlife == v.questionnaire.nightlife):
                    matching_points = matching_points + 5
                elif (u.questionnaire.nightlife != v.questionnaire.nightlife):
                    matching_points = matching_points + 1

                # STUDY ENVIRONMENTS
                if (u.questionnaire.study == v.questionnaire.study):
                    matching_points += 5
                elif (u.questionnaire.study != v.questionnaire.study):
                    matching_points += 1 
                
                # ON-/OFF-GROUNDS
                # If the same preference, +5. If one doesn't care, +3. If both have different preferences, +1. 
                if (u.questionnaire.where == v.questionnaire.where):
                    matching_points += 5
                elif (u.questionnaire.where == "I have no preference" or v.questionnaire.where == "I have no preference"):
                    matching_points += 3
                else:
                    matching_points += 1

                # PERSONALITY 
                if (u.questionnaire.personality == v.questionnaire.personality):
                    matching_points += 5
                else:
                    matching_points += 1

                # SHARING
                if (u.questionnaire.sharing == v.questionnaire.sharing):
                    matching_points += 5
                else:
                    matching_points += 1

                # ROOMING WITH OTHER GENDERS
                if (u.questionnaire.gender == v.questionnaire.gender):
                    matching_points += 5
                else:
                    matching_points += 1

                # ROOMING WITH OTHER YEARS
                if (u.questionnaire.year == v.questionnaire.year):
                    matching_points += 5
                else:
                    matching_points += 1
        #return the total amount of points from the questionnaure

                # Joshua Dano - 4/12/21 - Saving matches in a dataset
                #matching_points = 10
                matches[u] = [v, matching_points]
                matching_points = 0
                print("v", v)
    
    #matches won't display as a context do not know why.
    #print(matches)
    #print('--------------Now Printing All()--------------')
    #print(User.objects.all())
    #matches = sorted(matches.items(), key=matches.values()[1])

    return matches




















'''
def matching_set(self):
    #keeps track of the number of matched points
    matches = {}
    user_set = User.objects.all()
    matching_points = 0
    for u in user_set:
        for v in user_set:
            #Roommate choice is based on a ranking. If there is a no difference between the number, ex. [0,0] 
            #then there is 5 points added. If there is one difference: +4; two difference: +3; three 
            #difference: +2, and four/five difference: +1

            if (u.questionnaire.RoomatesChoice.FIVE) and  (v.questionnaire.RoomatesChoice.FIVE):
                matching_points = matching_points  + 5
            if (u.questionnaire.RoomatesChoice.FIVE) and  (v.questionnaire.RoomatesChoice.FOUR):
                matching_points = matching_points  + 4
            if (u.questionnaire.RoomatesChoice.FIVE) and  (v.questionnaire.RoomatesChoice.THREE):
                matching_points = matching_points  + 3
            if (u.questionnaire.RoomatesChoice.FIVE) and  (v.questionnaire.RoomatesChoice.TWO):
                matching_points = matching_points  + 2
            if (u.questionnaire.RoomatesChoice.FIVE) and  (v.questionnaire.RoomatesChoice.ONE):
                matching_points = matching_points  + 1
            if (u.questionnaire.RoomatesChoice.FIVE) and  (v.questionnaire.RoomatesChoice.ZERO):
                matching_points = matching_points  + 1

            if (u.questionnaire.RoomatesChoice.FOUR) and  (v.questionnaire.RoomatesChoice.FIVE):
                matching_points = matching_points  + 4
            if (u.questionnaire.RoomatesChoice.FOUR) and  (v.questionnaire.RoomatesChoice.FOUR):
                matching_points = matching_points  + 5
            if (u.questionnaire.RoomatesChoice.FOUR) and  (v.questionnaire.RoomatesChoice.THREE):
                matching_points = matching_points  + 4
            if (u.questionnaire.RoomatesChoice.FOUR) and  (v.questionnaire.RoomatesChoice.TWO):
                matching_points = matching_points  + 3
            if (u.questionnaire.RoomatesChoice.FOUR) and  (v.questionnaire.RoomatesChoice.ONE):
                matching_points = matching_points  + 2
            if (u.questionnaire.RoomatesChoice.FOUR) and  (v.questionnaire.RoomatesChoice.ZERO):
                matching_points = matching_points  + 1

            if (u.questionnaire.RoomatesChoice.THREE) and  (v.questionnaire.RoomatesChoice.FIVE):
                matching_points = matching_points  + 3
            if (u.questionnaire.RoomatesChoice.THREE) and  (v.questionnaire.RoomatesChoice.FOUR):
                matching_points = matching_points  + 4
            if (u.questionnaire.RoomatesChoice.THREE) and  (v.questionnaire.RoomatesChoice.THREE):
                matching_points = matching_points  + 5
            if (u.questionnaire.RoomatesChoice.THREE) and  (v.questionnaire.RoomatesChoice.TWO):
                matching_points = matching_points  + 4
            if (u.questionnaire.RoomatesChoice.THREE) and  (v.questionnaire.RoomatesChoice.ONE):
                matching_points = matching_points  + 3
            if (u.questionnaire.RoomatesChoice.THREE) and  (v.questionnaire.RoomatesChoice.ZERO):
                matching_points = matching_points  + 2

            if (u.questionnaire.RoomatesChoice.TWO) and  (v.questionnaire.RoomatesChoice.FIVE):
                matching_points = matching_points  + 2
            if (u.questionnaire.RoomatesChoice.TWO) and  (v.questionnaire.RoomatesChoice.FOUR):
                matching_points = matching_points  + 3
            if (u.questionnaire.RoomatesChoice.TWO) and  (v.questionnaire.RoomatesChoice.THREE):
                matching_points = matching_points  + 4
            if (u.questionnaire.RoomatesChoice.TWO) and  (v.questionnaire.RoomatesChoice.TWO):
                matching_points = matching_points  + 5
            if (u.questionnaire.RoomatesChoice.TWO) and  (v.questionnaire.RoomatesChoice.ONE):
                matching_points = matching_points  + 4
            if (u.questionnaire.RoomatesChoice.TWO) and  (v.questionnaire.RoomatesChoice.ZERO):
                matching_points = matching_points  + 3

            if (u.questionnaire.RoomatesChoice.ONE) and  (v.questionnaire.RoomatesChoice.FIVE):
                matching_points = matching_points  + 1
            if (u.questionnaire.RoomatesChoice.ONE) and  (v.questionnaire.RoomatesChoice.FOUR):
                matching_points = matching_points  + 2
            if (u.questionnaire.RoomatesChoice.ONE) and  (v.questionnaire.RoomatesChoice.THREE):
                matching_points = matching_points  + 3
            if (u.questionnaire.RoomatesChoice.ONE) and  (v.questionnaire.RoomatesChoice.TWO):
                matching_points = matching_points  + 4
            if (u.questionnaire.RoomatesChoice.ONE) and  (v.questionnaire.RoomatesChoice.ONE):
                matching_points = matching_points  + 5
            if (u.questionnaire.RoomatesChoice.ONE) and  (v.questionnaire.RoomatesChoice.ZERO):
                matching_points = matching_points  + 4

            if (u.questionnaire.RoomatesChoice.ZERO) and  (v.questionnaire.RoomatesChoice.FIVE):
                matching_points = matching_points  + 1
            if (u.questionnaire.RoomatesChoice.ZERO) and  (v.questionnaire.RoomatesChoice.FOUR):
                matching_points = matching_points  + 1
            if (u.questionnaire.RoomatesChoice.ZERO) and  (v.questionnaire.RoomatesChoice.THREE):
                matching_points = matching_points  + 2
            if (u.questionnaire.RoomatesChoice.ZERO) and  (v.questionnaire.RoomatesChoice.TWO):
                matching_points = matching_points  + 3
            if (u.questionnaire.RoomatesChoice.ZERO) and  (v.questionnaire.RoomatesChoice.ONE):
                matching_points = matching_points  + 4
            if (u.questionnaire.RoomatesChoice.ZERO) and  (v.questionnaire.RoomatesChoice.ZERO):
                matching_points = matching_points  + 5
            #if the same dorm preferences is said, then they have a high chance of matching, matching with no
            #preference is a normal match, two different styles is almost no points
            if (u.questionnaire.DormChoice == v.questionnaire.DormChoice):
                matching_points = matching_points + 5
            if (u.questionnaire.DormChoice.NONE) and (v.questionnaire.DormChoice.HALL):
                matching_points = matching_points + 3
            if (u.questionnaire.DormChoice.HALL) and (v.questionnaire.DormChoice.NONE):
                matching_points = matching_points + 3
            if (u.questionnaire.DormChoice.NONE) and (v.questionnaire.DormChoice.SUITE):
                matching_points = matching_points + 3
            if (u.questionnaire.DormChoice.SUITE) and (v.questionnaire.DormChoice.NONE):
                matching_points = matching_points + 3
            if (u.questionnaire.DormChoice.HALL) and (v.questionnaire.DormChoice.SUITE):
                matching_points = matching_points + 1
            if (u.questionnaire.DormChoice.SUITE) and (v.questionnaire.DormChoice.HALL):
                matching_points = matching_points + 1
            # Night owls and morning birds that match together [night owl, night owl] or [early bird, early bird]
            #will match high, either one and a neither will have a decent matching, and mix-matches have a low score
            if (u.questionnaire.time_of_day == "I'm a night owl") and (v.questionnaire.time_of_day == "I'm a night owl"):
                matching_points = matching_points + 5
            if (u.questionnaire.time_of_day == "I'm more of a morning person") and (v.questionnaire.time_of_day == "I'm more of a morning person"):
                matching_points = matching_points + 5
            if (u.questionnaire.time_of_day == "I'm a night owl") and (v.questionnaire.time_of_day == "Neither a night owl or early bird"):
                matching_points = matching_points + 3
            if (u.questionnaire.time_of_day == "Neither a night owl or early bird") and (v.questionnaire.time_of_day == "I'm a night owl"):
                matching_points = matching_points + 3
            if (u.questionnaire.time_of_day == "I'm more of a morning person") and (v.questionnaire.time_of_day == "Neither a night owl or early bird"):
                matching_points = matching_points + 3
            if (u.questionnaire.time_of_day == "Neither a night owl or early bird") and (v.questionnaire.time_of_day == "I'm more of a morning person"):
                matching_points = matching_points + 3
            if (u.questionnaire.time_of_day == "I'm a night owl") and (v.questionnaire.time_of_day == "I'm more of a morning person"):
                matching_points = matching_points + 1
            if (u.questionnaire.time_of_day == "I'm more of a morning person") and (v.questionnaire.time_of_day == "I'm a night owl"):
                matching_points = matching_points + 1
            # matching is similar to above. Messy and clean people that match together [clean, clean] or [messy,
            # messy] will match high, either one and a neither will have a decent matching, and mix-matches
            # #have a low score
            if (u.questionnaire.tidiness == "I'm a more messy person") and (v.questionnaire.tidiness == "I'm a more messy person"):
                matching_points = matching_points + 5
            if (u.questionnaire.tidiness == "I'm more of clean person") and (v.questionnaire.tidiness == "I'm more of clean person"):
                matching_points = matching_points + 5
            if (u.questionnaire.tidiness == "I'm a more messy person") and (v.questionnaire.tidiness == "I'm not overly clean nor messy"):
                matching_points = matching_points + 3
            if (u.questionnaire.tidiness == "I'm not overly clean nor messy") and (v.questionnaire.tidiness == "I'm a more messy person"):
                matching_points = matching_points + 3
            if (u.questionnaire.tidiness == "I'm more of clean person") and (v.questionnaire.tidiness == "I'm not overly clean nor messy"):
                matching_points = matching_points + 3
            if (u.questionnaire.tidiness == "I'm not overly clean nor messy") and (v.questionnaire.tidiness == "I'm more of clean person"):
                matching_points = matching_points + 3
            if (u.questionnaire.tidiness == "I'm more of clean person") and (v.questionnaire.tidiness == "I'm a more messy person"):
                matching_points = matching_points + 1
            if (u.questionnaire.tidiness == "I'm a more messy person") and (v.questionnaire.tidiness == "I'm more of clean person"):
                matching_points = matching_points + 1
            #matching [yes, yes] an [no, no] will have high scores, and mix matches will have low scores
            if (u.questionnaire.SmokeDrinkChoice.YES) and (v.questionnaire.SmokeDrinkChoice.YES):
                matching_points = matching_points + 5
            if (u.questionnaire.SmokeDrinkChoice.NO) and (v.questionnaire.SmokeDrinkChoice.NO):
                matching_points = matching_points + 5
            if (u.questionnaire.SmokeDrinkChoice.YES) and (v.questionnaire.SmokeDrinkChoice.NO):
                matching_points = matching_points + 1
            if (u.questionnaire.SmokeDrinkChoice.NO) and (v.questionnaire.SmokeDrinkChoice.YES):
                matching_points = matching_points + 1
            # matching [yes, yes] an [no, no] will have high scores, and mix matches will have low scores
            if (u.questionnaire.OvernightChoice.YES) and (v.questionnaire.OvernightChoice.YES):
                matching_points = matching_points + 5
            if (u.questionnaire.OvernightChoice.NO) and (v.questionnaire.OvernightChoice.NO):
                matching_points = matching_points + 5
            if (u.questionnaire.OvernightChoice.YES) and (v.questionnaire.OvernightChoice.NO):
                matching_points = matching_points + 1
            if (u.questionnaire.OvernightChoice.NO) and (v.questionnaire.OvernightChoice.YES):
                matching_points = matching_points + 1
            # matching [yes, yes] an [no, no] will have high scores, and mix matches will have low scores
            if (u.questionnaire.NightlifeChoice.YES) and (v.questionnaire.NightlifeChoice.YES):
                matching_points = matching_points + 5
            if (u.questionnaire.NightlifeChoice.NO) and (v.questionnaire.NightlifeChoice.NO):
                matching_points = matching_points + 5
            if (u.questionnaire.NightlifeChoice.YES) and (v.questionnaire.NightlifeChoice.NO):
                matching_points = matching_points + 1
            if (u.questionnaire.NightlifeChoice.NO) and (v.questionnaire.NightlifeChoice.YES):
                matching_points = matching_points + 1
            # matching [quiet, quiet] an [loud, loud] will have high scores, and mix matches will have low scores
            if (u.questionnaire.StudyChoice.QUIET) and (v.questionnaire.StudyChoice.QUIET):
                matching_points = matching_points + 5
            if (u.questionnaire.StudyChoice.LOUD) and (v.questionnaire.StudyChoice.QUIET):
                matching_points = matching_points + 5
            if (u.questionnaire.StudyChoice.QUIET) and (v.questionnaire.StudyChoice.LOUD):
                matching_points = matching_points + 1
            if (u.questionnaire.StudyChoice.LOUD) and (v.questionnaire.StudyChoice.QUIET):
                matching_points = matching_points + 1
            # matching is similar to above. Off grounds and on grounds people that match together [on, on] or [off,
            # off] will match high, either one and a neither will have a decent matching, and mix-matches
            # #have a low score
            if (u.questionnaire.WhereChoice.ON_GROUNDS) and (v.questionnaire.WhereChoice.ON_GROUNDS):
                matching_points = matching_points + 5
            if (u.questionnaire.WhereChoice.OFF_GROUNDS) and (v.questionnaire.WhereChoice.OFF_GROUNDS):
                matching_points = matching_points + 5
            if (u.questionnaire.WhereChoice.ON_GROUNDS) and (v.questionnaire.WhereChoice.NO_PREF):
                matching_points = matching_points + 3
            if (u.questionnaire.WhereChoice.NO_PREF) and (v.questionnaire.WhereChoice.ON_GROUNDS):
                matching_points = matching_points + 3
            if (u.questionnaire.WhereChoice.OFF_GROUNDS) and (v.questionnaire.WhereChoice.NO_PREF):
                matching_points = matching_points + 3
            if (u.questionnaire.WhereChoice.NO_PREF) and (v.questionnaire.WhereChoice.OFF_GROUNDS):
                matching_points = matching_points + 3
            if (u.questionnaire.WhereChoice.ON_GROUNDS) and (v.questionnaire.WhereChoice.OFF_GROUNDS):
                matching_points = matching_points + 1
            if (u.questionnaire.WhereChoice.OFF_GROUNDS) and (v.questionnaire.WhereChoice.ON_GROUNDS):
                matching_points = matching_points + 1
            # matching [extrovert, extrovert] an [introvert, introvert] will have high scores, and mix matches will have low scores
            if (u.questionnaire.PersonalityChoice.EXTROVERT) and (v.questionnaire.PersonalityChoice.EXTROVERT):
                matching_points = matching_points + 5
            if (u.questionnaire.PersonalityChoice.INTROVERT) and (v.questionnaire.PersonalityChoice.INTROVERT):
                matching_points = matching_points + 5
            if (u.questionnaire.PersonalityChoice.INTROVERT) and (v.questionnaire.PersonalityChoice.EXTROVERT):
                matching_points = matching_points + 1
            if (u.questionnaire.PersonalityChoice.EXTROVERT) and (v.questionnaire.PersonalityChoice.INTROVERT):
                matching_points = matching_points + 1
            # matching [yes, yes] an [no, no] will have high scores, and mix matches will have low scores
            if (u.questionnaire.SharingChoice.YES) and (v.questionnaire.SharingChoice.YES):
                matching_points = matching_points + 5
            if (u.questionnaire.SharingChoice.NO) and (v.questionnaire.SharingChoice.NO):
                matching_points = matching_points + 5
            if (u.questionnaire.SharingChoice.NO) and (v.questionnaire.SharingChoice.YES):
                matching_points = matching_points + 1
            if (u.questionnaire.SharingChoice.YES) and (v.questionnaire.SharingChoice.NO):
                matching_points = matching_points + 1
            # matching [yes, yes] an [no, no] will have high scores, and mix matches will have low scores
            if (u.questionnaire.GenderChoice.YES) and (v.questionnaire.GenderChoice.YES):
                matching_points = matching_points + 5
            if (u.questionnaire.GenderChoice.NO) and (v.questionnaire.GenderChoice.NO):
                matching_points = matching_points + 5
            if (u.questionnaire.GenderChoice.NO) and (v.questionnaire.GenderChoice.YES):
                matching_points = matching_points + 1
            if (u.questionnaire.GenderChoice.YES) and (v.questionnaire.GenderChoice.NO):
                matching_points = matching_points + 1
            # matching [yes, yes] an [no, no] will have high scores, and mix matches will have low scores
            if (u.questionnaire.YearChoice.YES) and (v.questionnaire.YearChoice.YES):
                matching_points = matching_points + 5
            if (u.questionnaire.YearChoice.NO) and (v.questionnaire.YearChoice.NO):
                matching_points = matching_points + 5
            if (u.questionnaire.YearChoice.NO) and (v.questionnaire.YearChoice.YES):
                matching_points = matching_points + 1
            if (u.questionnaire.YearChoice.YES) and (v.questionnaire.YearChoice.NO):
                matching_points = matching_points + 1
    #return the total amount of points from the questionnaure

            # Joshua Dano - 4/12/21 - Saving matches in a dataset
            matches[tuple([u, v])] = matching_points

    # Joshua Dano - 4/12/21 - Idea for finding the best match
    top_3_per_user = {}
    for user in user_set:
        top_3 = find_best_match(user, matches)
        top_3_per_user[user] = top_3

    return top_3_per_user # this will be a dictionary with the key being an individual and the value being a list of the top 3 users

# pairs = {['josh', 'campbell']: 10, ['abigail', 'josh']: 9, ['abigail', 'campbell']: 15, ['campbell', 'juliette']: 8}
# find_best_match('josh', pairs)
def find_best_match(user, pairs):
    matches = {}
    for pair in pairs:
            if user in pair: # pair is a list of two users
                if user == pair[0]: 
                    matches[pair[1]] = pairs[pair]
                else: 
                    matches[pair[0]] = pairs[pair]
    
    # matches = {'campbell': 10, 'abigail': 11, 'juliette': 6, 'alex': 20}

    # source: https://stackoverflow.com/questions/40496518/how-to-get-the-3-items-with-the-highest-value-from-dictionary
    top_3 = sorted(matches, key=matches.get, reverse = True)[:3]
    
    return top_3
'''