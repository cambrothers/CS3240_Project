from django.test import TestCase

from .models import Profile
#from .models import  DormChoice
#from .models import SchoolChoice

# Create your tests here.

class CreateProfileTest(TestCase):
    """
    Prints that you can continue making your account if a name has been entered
    """
    def setUp_with_name(self):
        create_name = User.objects.create(name="Sarah")
        if (self.assertEqual(create_name, "Sarah"), True):
            print("You can save your account")
        

    """
    Prints that you cannot continue making your account if a name has not been entered 
    """
    def setUp_without_name(self):
        no_name = User.objects.create(name="blank")
        if (self.assertIs(no_name, "Sarah"), False):
            print("You have not entered a name. You must enter a name to save your profile.")

    """
    Return true if the email address given for the account is unique
    """
    def profile_is_unique(self):
        user_name = User.objects.create(name="Sarah")
        user_email = User._meta.get_field('email')._unique
        if(self.assertEqual(user_email, True)== True):
            print("You can continue creating an account as you have made an email")

    """
    Return false if an email was not given for the account is blank
    """

    def profile_is_not_unique(self):
        user_name = Usesr.objects.create(name="Sarah") 
        user_email = User._meta.get_field('email').blank
        if (self.assertEqual(user_email, False)==False):
            print("You cannot continue creating an account as you have not entered an email")

        user_email_null = User._meta.get_field('email').null    
        if (self.assertEqual(user_email_null, True)!= False):
            print("You cannot continue creating an account as you have not entered an email")  

    """
    Prints that you have can continue your account because you have a name and email
    """
    def setUp_with_name_email(self):
        create_name = User.objects.create(name="Sarah")
        create_email = User._meta.get_field('email')._unique
        if (self.assertEqual(create_email, True)==True):
            print("You can continue creatng an account as you have entered correct info")

    



    

