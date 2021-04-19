from django.contrib.auth import get_user_model
from django.test import TestCase
from django.contrib.auth.models import  User
from .models import Profile
# from .models import DormChoice
# from .models import SchoolChoice


# Create your tests here.

class CreateProfileTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(user="new_user", name="user")

    """
    Test to see if the profile created is valid 
    """
    def test_Profile_Correct(self):
        form = User(data={'user':"new_user", 'name':"name"})
        self.assertTrue(form.is_valid())
    """
    Test to see if the profile created is valid [should be invalid]"""
    def test_Profile_Incorrect(self):
        form = User(data={'user':"new_user", 'name':""})
        self.assertTrue(form.isvalid())

    def test_assert(self):
        self.assertTrue(True)

    def test_assert(self):
        self.assertFalse(True)


class CreateQuestionnaireTestCases(TestCase):
    def setUp(self):
        self.questionnaire = User.objects.create(number_of_roommates=2, dorm_pref)

    def setUp_Questionnaire(self):
        questionnaire = Questionnaire()








