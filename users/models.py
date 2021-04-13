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