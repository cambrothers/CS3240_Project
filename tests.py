import unittest
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from users.models import Profile

#def create_user =

class ProfileCreate(TestCase):

    def test_dummy(self):
        self.assertTrue(True)
#
#     def test_is_username(self):
#         User.objects.create_user(username= 'user')

# class UserTest(unittest.TestCase):
#     def test_setUp(self):
#         self.user = User.objects.create_superuser(self.username, self.email, self.password)
#         self.assertEqual(self.user.username, 'user')
#         print(self.user.username)
#         # self.assertTrue(self.user.first_name, 'name')
#         # print(self.user.first_name)

class ProfileTest(unittest.TestCase):
    def test_required_name(self):
        print("Before the no_name test")
        # #no_name = Profile.objects.create(name='')
        # name = Profile.name
        #
        # self.assertEqual(name, 'name')
        print("You need to go back a place your name")

class ViewTest(unittest.TestCase):
    def test_setUp(self):
        self.factory = RequestFactory
        self.user = User.objects.create_user(username='name', email='user@example.com',  password='password')

    # def test_details(self):
    #     request = self.factory.get('/users/users/profile')
    #     request.user = self.user

class ScheduleTest(unittest.TestCase)

