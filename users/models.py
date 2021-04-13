from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from CS3240_A20 import settings

#May need to pip install django-imagekit if import statements aren't working. Note imagekit depends on Pillow.
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, SmartResize
from PIL import Image

# Create your models here.
User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField( upload_to="images/", default="media/images/noimage_rb51dj.png")
    name = models.CharField(max_length=400)
    bio = models.CharField(max_length=500,blank=True,default="")
    pronouns = models.CharField(max_length=400,blank=True,default="")
    age = models.PositiveIntegerField(default=17,blank=True)
    year = models.PositiveIntegerField(default=1,blank=True)

    schedule_image = models.ImageField( upload_to="images/",default="media/images/noschedule_zdconk.png")
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
    def __str__(self):
        return f'{self.user.username} Profile'


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

#Campbell Brothers: 4/11 Adding a matching algorithm to the questionnaire

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
                if (u.Questionnaire.RoomatesChoice.FIVE) and  (v.Questionnaire.RoomatesChoice.FIVE):
                    matching_points = matching_points  + 5
                if (u.Questionnaire.RoomatesChoice.FIVE) and  (v.Questionnaire.RoomatesChoice.FOUR):
                    matching_points = matching_points  + 4
                if (u.Questionnaire.RoomatesChoice.FIVE) and  (v.Questionnaire.RoomatesChoice.THREE):
                    matching_points = matching_points  + 3
                if (u.Questionnaire.RoomatesChoice.FIVE) and  (v.Questionnaire.RoomatesChoice.TWO):
                    matching_points = matching_points  + 2
                if (u.Questionnaire.RoomatesChoice.FIVE) and  (v.Questionnaire.RoomatesChoice.ONE):
                    matching_points = matching_points  + 1
                if (u.Questionnaire.RoomatesChoice.FIVE) and  (v.Questionnaire.RoomatesChoice.ZERO):
                    matching_points = matching_points  + 1

                if (u.Questionnaire.RoomatesChoice.FOUR) and  (v.Questionnaire.RoomatesChoice.FIVE):
                    matching_points = matching_points  + 4
                if (u.Questionnaire.RoomatesChoice.FOUR) and  (v.Questionnaire.RoomatesChoice.FOUR):
                    matching_points = matching_points  + 5
                if (u.Questionnaire.RoomatesChoice.FOUR) and  (v.Questionnaire.RoomatesChoice.THREE):
                    matching_points = matching_points  + 4
                if (u.Questionnaire.RoomatesChoice.FOUR) and  (v.Questionnaire.RoomatesChoice.TWO):
                    matching_points = matching_points  + 3
                if (u.Questionnaire.RoomatesChoice.FOUR) and  (v.Questionnaire.RoomatesChoice.ONE):
                    matching_points = matching_points  + 2
                if (u.Questionnaire.RoomatesChoice.FOUR) and  (v.Questionnaire.RoomatesChoice.ZERO):
                    matching_points = matching_points  + 1

                if (u.Questionnaire.RoomatesChoice.THREE) and  (v.Questionnaire.RoomatesChoice.FIVE):
                    matching_points = matching_points  + 3
                if (u.Questionnaire.RoomatesChoice.THREE) and  (v.Questionnaire.RoomatesChoice.FOUR):
                    matching_points = matching_points  + 4
                if (u.Questionnaire.RoomatesChoice.THREE) and  (v.Questionnaire.RoomatesChoice.THREE):
                    matching_points = matching_points  + 5
                if (u.Questionnaire.RoomatesChoice.THREE) and  (v.Questionnaire.RoomatesChoice.TWO):
                    matching_points = matching_points  + 4
                if (u.Questionnaire.RoomatesChoice.THREE) and  (v.Questionnaire.RoomatesChoice.ONE):
                    matching_points = matching_points  + 3
                if (u.Questionnaire.RoomatesChoice.THREE) and  (v.Questionnaire.RoomatesChoice.ZERO):
                    matching_points = matching_points  + 2

                if (u.Questionnaire.RoomatesChoice.TWO) and  (v.Questionnaire.RoomatesChoice.FIVE):
                    matching_points = matching_points  + 2
                if (u.Questionnaire.RoomatesChoice.TWO) and  (v.Questionnaire.RoomatesChoice.FOUR):
                    matching_points = matching_points  + 3
                if (u.Questionnaire.RoomatesChoice.TWO) and  (v.Questionnaire.RoomatesChoice.THREE):
                    matching_points = matching_points  + 4
                if (u.Questionnaire.RoomatesChoice.TWO) and  (v.Questionnaire.RoomatesChoice.TWO):
                    matching_points = matching_points  + 5
                if (u.Questionnaire.RoomatesChoice.TWO) and  (v.Questionnaire.RoomatesChoice.ONE):
                    matching_points = matching_points  + 4
                if (u.Questionnaire.RoomatesChoice.TWO) and  (v.Questionnaire.RoomatesChoice.ZERO):
                    matching_points = matching_points  + 3

                if (u.Questionnaire.RoomatesChoice.ONE) and  (v.Questionnaire.RoomatesChoice.FIVE):
                    matching_points = matching_points  + 1
                if (u.Questionnaire.RoomatesChoice.ONE) and  (v.Questionnaire.RoomatesChoice.FOUR):
                    matching_points = matching_points  + 2
                if (u.Questionnaire.RoomatesChoice.ONE) and  (v.Questionnaire.RoomatesChoice.THREE):
                    matching_points = matching_points  + 3
                if (u.Questionnaire.RoomatesChoice.ONE) and  (v.Questionnaire.RoomatesChoice.TWO):
                    matching_points = matching_points  + 4
                if (u.Questionnaire.RoomatesChoice.ONE) and  (v.Questionnaire.RoomatesChoice.ONE):
                    matching_points = matching_points  + 5
                if (u.Questionnaire.RoomatesChoice.ONE) and  (v.Questionnaire.RoomatesChoice.ZERO):
                    matching_points = matching_points  + 4

                if (u.Questionnaire.RoomatesChoice.ZERO) and  (v.Questionnaire.RoomatesChoice.FIVE):
                    matching_points = matching_points  + 1
                if (u.Questionnaire.RoomatesChoice.ZERO) and  (v.Questionnaire.RoomatesChoice.FOUR):
                    matching_points = matching_points  + 1
                if (u.Questionnaire.RoomatesChoice.ZERO) and  (v.Questionnaire.RoomatesChoice.THREE):
                    matching_points = matching_points  + 2
                if (u.Questionnaire.RoomatesChoice.ZERO) and  (v.Questionnaire.RoomatesChoice.TWO):
                    matching_points = matching_points  + 3
                if (u.Questionnaire.RoomatesChoice.ZERO) and  (v.Questionnaire.RoomatesChoice.ONE):
                    matching_points = matching_points  + 4
                if (u.Questionnaire.RoomatesChoice.ZERO) and  (v.Questionnaire.RoomatesChoice.ZERO):
                    matching_points = matching_points  + 5
                #if the same dorm preferences is said, then they have a high chance of matching, matching with no
                #preference is a normal match, two different styles is almost no points
                if (u.Questionnaire.DormChoice == v.Questionnaire.DormChoice):
                    matching_points = matching_points + 5
                if (u.Questionnaire.DormChoice.NONE) and (v.Questionnaire.DormChoice.HALL):
                    matching_points = matching_points + 3
                if (u.Questionnaire.DormChoice.HALL) and (v.Questionnaire.DormChoice.NONE):
                    matching_points = matching_points + 3
                if (u.Questionnaire.DormChoice.NONE) and (v.Questionnaire.DormChoice.SUITE):
                    matching_points = matching_points + 3
                if (u.Questionnaire.DormChoice.SUITE) and (v.Questionnaire.DormChoice.NONE):
                    matching_points = matching_points + 3
                if (u.Questionnaire.DormChoice.HALL) and (v.Questionnaire.DormChoice.SUITE):
                    matching_points = matching_points + 1
                if (u.Questionnaire.DormChoice.SUITE) and (v.Questionnaire.DormChoice.HALL):
                    matching_points = matching_points + 1
                # Night owls and morning birds that match together [night owl, night owl] or [early bird, early bird]
                #will match high, either one and a neither will have a decent matching, and mix-matches have a low score
                if (u.Questionnaire.TODChoice.NIGHT) and (v.Questionnaire.TODChoice.NIGHT):
                    matching_points = matching_points + 5
                if (u.Questionnaire.TODChoice.MORNING) and (v.Questionnaire.TODChoice.MORNING):
                    matching_points = matching_points + 5
                if (u.Questionnaire.TODChoice.NIGHT) and (v.Questionnaire.TODChoice.NEITHER):
                    matching_points = matching_points + 3
                if (u.Questionnaire.TODChoice.NEITHER) and (v.Questionnaire.TODChoice.NIGHT):
                    matching_points = matching_points + 3
                if (u.Questionnaire.TODChoice.MORNING) and (v.Questionnaire.TODChoice.NEITHER):
                    matching_points = matching_points + 3
                if (u.Questionnaire.TODChoice.NEITHER) and (v.Questionnaire.TODChoice.MORNING):
                    matching_points = matching_points + 3
                if (u.Questionnaire.TODChoice.NIGHT) and (v.Questionnaire.TODChoice.MORNING):
                    matching_points = matching_points + 1
                if (u.Questionnaire.TODChoice.MORNING) and (v.Questionnaire.TODChoice.NIGHT):
                    matching_points = matching_points + 1
                # matching is similar to above. Messy and clean people that match together [clean, clean] or [messy,
                # messy] will match high, either one and a neither will have a decent matching, and mix-matches
                # #have a low score
                if (u.Questionnaire.TidinessChoice.MESSY) and (v.Questionnaire.TidinessChoice.MESSY):
                    matching_points = matching_points + 5
                if (u.Questionnaire.TidinessChoice.CLEAN) and (v.Questionnaire.TidinessChoice.CLEAN):
                    matching_points = matching_points + 5
                if (u.Questionnaire.TidinessChoice.MESSY) and (v.Questionnaire.TidinessChoice.NEITHER):
                    matching_points = matching_points + 3
                if (u.Questionnaire.TidinessChoice.NEITHER) and (v.Questionnaire.TidinessChoice.MESSY):
                    matching_points = matching_points + 3
                if (u.Questionnaire.TidinessChoice.CLEAN) and (v.Questionnaire.TidinessChoice.NEITHER):
                    matching_points = matching_points + 3
                if (u.Questionnaire.TidinessChoice.NEITHER) and (v.Questionnaire.TidinessChoice.CLEAN):
                    matching_points = matching_points + 3
                if (u.Questionnaire.TidinessChoice.CLEAN) and (v.Questionnaire.TidinessChoice.MESSY):
                    matching_points = matching_points + 1
                if (u.Questionnaire.TidinessChoice.MESSY) and (v.Questionnaire.TidinessChoice.CLEAN):
                    matching_points = matching_points + 1
                #matching [yes, yes] an [no, no] will have high scores, and mix matches will have low scores
                if (u.Questionnaire.SmokeDrinkChoice.YES) and (v.Questionnaire.SmokeDrinkChoice.Yes):
                    matching_points = matching_points + 5
                if (u.Questionnaire.SmokeDrinkChoice.NO) and (v.Questionnaire.SmokeDrinkChoice.NO):
                    matching_points = matching_points + 5
                if (u.Questionnaire.SmokeDrinkChoice.YES) and (v.Questionnaire.SmokeDrinkChoice.NO):
                    matching_points = matching_points + 1
                if (u.Questionnaire.SmokeDrinkChoice.NO) and (v.Questionnaire.SmokeDrinkChoice.Yes):
                    matching_points = matching_points + 1
                # matching [yes, yes] an [no, no] will have high scores, and mix matches will have low scores
                if (u.Questionnaire.OvernightChoice.YES) and (v.Questionnaire.OvernightChoice.Yes):
                    matching_points = matching_points + 5
                if (u.Questionnaire.OvernightChoice.NO) and (v.Questionnaire.OvernightChoice.NO):
                    matching_points = matching_points + 5
                if (u.Questionnaire.OvernightChoice.YES) and (v.Questionnaire.OvernightChoice.NO):
                    matching_points = matching_points + 1
                if (u.Questionnaire.OvernightChoice.NO) and (v.Questionnaire.OvernightChoice.Yes):
                    matching_points = matching_points + 1
                # matching [yes, yes] an [no, no] will have high scores, and mix matches will have low scores
                if (u.Questionnaire.NightlifeChoice.YES) and (v.Questionnaire.NightlifeChoice.Yes):
                    matching_points = matching_points + 5
                if (u.Questionnaire.NightlifeChoice.NO) and (v.Questionnaire.NightlifeChoice.NO):
                    matching_points = matching_points + 5
                if (u.Questionnaire.NightlifeChoice.YES) and (v.Questionnaire.NightlifeChoice.NO):
                    matching_points = matching_points + 1
                if (u.Questionnaire.NightlifeChoice.NO) and (v.Questionnaire.NightlifeChoice.Yes):
                    matching_points = matching_points + 1
                # matching [quiet, quiet] an [loud, loud] will have high scores, and mix matches will have low scores
                if (u.Questionnaire.StudyChoice.QUIET) and (v.Questionnaire.StudyChoice.QUIET):
                    matching_points = matching_points + 5
                if (u.Questionnaire.StudyChoice.LOUD) and (v.Questionnaire.StudyChoice.QUIET):
                    matching_points = matching_points + 5
                if (u.Questionnaire.StudyChoice.QUIET) and (v.Questionnaire.StudyChoice.LOUD):
                    matching_points = matching_points + 1
                if (u.Questionnaire.StudyChoice.LOUD) and (v.Questionnaire.StudyChoice.QUIET):
                    matching_points = matching_points + 1
                # matching is similar to above. Off grounds and on grounds people that match together [on, on] or [off,
                # off] will match high, either one and a neither will have a decent matching, and mix-matches
                # #have a low score
                if (u.Questionnaire.WhereChoice.ON_GROUNDS) and (v.Questionnaire.WhereChoice.ON_GROUNDS):
                    matching_points = matching_points + 5
                if (u.Questionnaire.WhereChoice.OFF_GROUNDS) and (v.Questionnaire.WhereChoice.OFF_GROUNDS):
                    matching_points = matching_points + 5
                if (u.Questionnaire.WhereChoice.ON_GROUNDS) and (v.Questionnaire.WhereChoice.NO_PREF):
                    matching_points = matching_points + 3
                if (u.Questionnaire.WhereChoice.NO_PREF) and (v.Questionnaire.WhereChoice.ON_GROUNDS):
                    matching_points = matching_points + 3
                if (u.Questionnaire.WhereChoice.OFF_GROUNDS) and (v.Questionnaire.WhereChoice.NO_PREF):
                    matching_points = matching_points + 3
                if (u.Questionnaire.WhereChoice.NO_PREF) and (v.Questionnaire.WhereChoice.OFF_GROUNDS):
                    matching_points = matching_points + 3
                if (u.Questionnaire.WhereChoice.ON_GROUNDS) and (v.Questionnaire.WhereChoice.OFF_GROUNDS):
                    matching_points = matching_points + 1
                if (u.Questionnaire.WhereChoice.OFF_GROUNDS) and (v.Questionnaire.WhereChoice.ON_GROUNDS):
                    matching_points = matching_points + 1
                # matching [extrovert, extrovert] an [introvert, introvert] will have high scores, and mix matches will have low scores
                if (u.Questionnaire.PersonalityChoice.EXTROVERT) and (v.Questionnaire.PersonalityChoice.EXTROVERT):
                    matching_points = matching_points + 5
                if (u.Questionnaire.PersonalityChoice.INTROVERT) and (v.Questionnaire.PersonalityChoice.INTROVERT):
                    matching_points = matching_points + 5
                if (u.Questionnaire.PersonalityChoice.INTROVERT) and (v.Questionnaire.PersonalityChoice.EXTROVERT):
                    matching_points = matching_points + 1
                if (u.Questionnaire.PersonalityChoice.EXTROVERT) and (v.Questionnaire.PersonalityChoice.INTROVERT):
                    matching_points = matching_points + 1
                # matching [yes, yes] an [no, no] will have high scores, and mix matches will have low scores
                if (u.Questionnaire.SharingChoice.YES) and (v.Questionnaire.SharingChoice.YES):
                    matching_points = matching_points + 5
                if (u.Questionnaire.SharingChoice.NO) and (v.Questionnaire.SharingChoice.NO):
                    matching_points = matching_points + 5
                if (u.Questionnaire.SharingChoice.NO) and (v.Questionnaire.SharingChoice.YES):
                    matching_points = matching_points + 1
                if (u.Questionnaire.SharingChoice.YES) and (v.Questionnaire.SharingChoice.NO):
                    matching_points = matching_points + 1
                # matching [yes, yes] an [no, no] will have high scores, and mix matches will have low scores
                if (u.Questionnaire.GenderChoice.YES) and (v.Questionnaire.GenderChoice.YES):
                    matching_points = matching_points + 5
                if (u.Questionnaire.GenderChoice.NO) and (v.Questionnaire.GenderChoice.NO):
                    matching_points = matching_points + 5
                if (u.Questionnaire.GenderChoice.NO) and (v.Questionnaire.GenderChoice.YES):
                    matching_points = matching_points + 1
                if (u.Questionnaire.GenderChoice.YES) and (v.Questionnaire.GenderChoice.NO):
                    matching_points = matching_points + 1
                # matching [yes, yes] an [no, no] will have high scores, and mix matches will have low scores
                if (u.Questionnaire.YearChoice.YES) and (v.Questionnaire.YearChoice.YES):
                    matching_points = matching_points + 5
                if (u.Questionnaire.YearChoice.NO) and (v.Questionnaire.YearChoice.NO):
                    matching_points = matching_points + 5
                if (u.Questionnaire.YearChoice.NO) and (v.Questionnaire.YearChoice.YES):
                    matching_points = matching_points + 1
                if (u.Questionnaire.YearChoice.YES) and (v.Questionnaire.YearChoice.NO):
                    matching_points = matching_points + 1
        #return the total amount of points from the questionnaure

                # Joshua Dano - 4/12/21 - Saving matches in a dataset
                matches[[u, v]] = matching_points

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
