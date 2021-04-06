from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

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
    image = models.ImageField( upload_to="images/", default="/media/images/blank-profile-picture-973460_1280_jslnqr.png")
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
