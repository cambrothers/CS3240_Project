from django.test import TestCase
from django.contrib.auth.models import User

from .models import Profile
# from .models import DormChoice
# from .models import SchoolChoice

# Create your tests here.
def create_user(user, image, name, bio, pronouns, age, year):
    """
    Create a profile with the given profile information that can be entered in the account
    """
    return User.objects.create(user='sarah', image=image, name='Sarah', bio=bio, pronouns=pronouns, age=age, year=year)
    # User.objects.create(user=, name='blank')
    # User.objects.create(user='blank', name='blank')

class CreateProfileTestCase(TestCase):
    """
    Prints that you can continue making your account if a name has been entered
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_something_pass(self):
        self.assertFalse(False)

    def test_something_fail(self):
        self.assertTrue(False)

    def test_setUp_with_Profile(self):
        # name = User(name='Sarah')
        # user = User(user='sarah')

        if (name != 'blank') and (user != 'blank'):
            print("You have successfully created your account")
        else:
            print("Fill out your username and name before continuing")
        
        #user = User.objects.get(user='sarah')
        #self.assertEqual(name, 'Sarah')
        # self.assertIs(user, 'Sarah')

#
#     """
#     Prints that you cannot continue making your account if a name has not been entered
#     """
#     def setUp_without_name(self):
#         no_name = User.objects.create(name="blank")
#         if (self.assertIs(no_name, "Sarah"), False):
#             print("You have not entered a name. You must enter a name to save your profile.")
#
#     """
#     Return true if the email address given for the account is unique
#     """
#     def profile_is_unique(self):
#         user_name = User.objects.create(name="Sarah")
#         user_email = User._meta.get_field('email')._unique
#         if(self.assertEqual(user_email, True)== True):
#             print("You can continue creating an account as you have made an email")
#
#     """
#     Return false if an email was not given for the account is blank
#     """
#
#     def profile_is_not_unique(self):
#         user_name = User.objects.create(name="Sarah")
#         user_email = User._meta.get_field('email').blank
#         if (self.assertEqual(user_email, False)==False):
#             print("You cannot continue creating an account as you have not entered an email")
#
#         user_email_null = User._meta.get_field('email').null
#         if (self.assertEqual(user_email_null, True)!= False):
#             print("You cannot continue creating an account as you have not entered an email")
#
#     """
#     Prints that you have can continue your account because you have a name and email
#     """
#     def setUp_with_name_email(self):
#         create_name = User.objects.create(name="Sarah")
#         create_email = User._meta.get_field('email')._unique
#         if (self.assertEqual(create_email, True)==True):
#             print("You can continue creatng an account as you have entered correct info")
#
#
# class UploadingScheduleImage(TestCase):
#     """
#     Checking to make sure that a new image has been added to the users profile
#     """
#     def setUp_with_schedule(self):
#          if (self.assertEqual(Profile.schedule_image(default="media/images/noschedule_zdconk.png"), True), True):
#              print("Make sure to change the default schedule to your own schedule!")
#
#
# #Campbell Brothers, 4/12 creating a couple of profiles before working on the matching
# def create_profile_user_1(user, name, pronouns, age, year):
#     """
#     Create a profile with differents sets of information, but all must have the required
#     informtion to create a account
#     """
#     return User.objects.create(user=user, name=name, pronouns=pronouns, age=age, year=year)
#
# def create_profile_user_2(user, name, pronouns, bio, age, year):
#     """
#     Create a profile with differents sets of information, but all must have the required
#     informtion to create a account
#     """
#     return User.objects.create(user=user, name=name, pronouns=pronouns, bio=bio, age=age, year=year)
#
# def create_profile_user_3(user, name, age, year):
#     """
#     Create a profile with differents sets of information, but all must have the required
#     informtion to create a account
#     """
#     return User.objects.create(user=user, name=name, age=age, year=year)
#
# def create_profile_user_4(user, name, year):
#     """
#     Create a profile with differents sets of information, but all must have the required
#     informtion to create a account
#     """
#     return User.objects.create(user=user, name=name, year=year)
#
# def create_profile_user_5(user, name):
#     """
#     Create a profile with differents sets of information, but all must have the required
#     informtion to create a account
#     """
#     return User.objects.create(user=user, name=name)
#
# #testing for the algorithm
# class TestingMatchingAlgorithm(TestCase):
#     def pull_all_users(self):
#         user_set = User.objects.all()
#         print(user_set)
