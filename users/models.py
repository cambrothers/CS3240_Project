from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=400)
    bio = models.CharField(max_length=500)
    pronouns = models.CharField(max_length=400)
    age = models.PositiveIntegerField(default=17)
    year = models.PositiveIntegerField(default=1)
    class DormChoice(models.TextChoices):
        NONE = "No preference."
        HALL = "Hall-Style"
        SUITE = "Suite-Style"
    dorm_pref = models.CharField(max_length= 100,choices=DormChoice.choices,default=DormChoice.NONE)
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
      
    school = models.CharField(max_length= 500,choices=SchoolChoice.choices,default=SchoolChoice.DEFAULT)
    roomates = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f'{self.user.username} Profile'

