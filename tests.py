from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from users.models import Profile, Questionnaire, DiscussionThread
# from .views import DiscussionView

#def create_user =

class ProfileCreate(TestCase):
    """
    Quick test to see if the assert is working
    """
    def test_dummy(self):
        self.assertTrue(True)
#
#     def test_is_username(self):
#         User.objects.create_user(username= 'user')
    def tearDown(self):
        # Clean up run after every test method.
        pass
# class UserTest(unittest.TestCase):
        """
        Test to see if username works correctly
        """
    def test_setUp(self):
        self.user = User.objects.create_user(username='name', email='user@example.com',  password='password')
        self.assertEqual(self.user.username, 'name')
        print(self.user.username)
        # self.assertEqual(self.user.first_name, 'name')
#         # print(self.user.first_name)
    def tearDown(self):
        # Clean up run after every test method.
        pass

class ProfileTest(TestCase):
    def test_required_name(self):
        blank = ''
        print("Before the no_name test")
        self.name = Profile(name = 'name')
        # print(self.Profile.name)
        self.assertEqual(self.name, blank)

        def tearDown(self):
            # Clean up run after every test method.
            pass

        # name = Profile.name
        #
        # self.assertEqual(name, 'name')
        if (self.assertEqual(self.name, blank) == True):
            print("You need to go back a place your name")

        def tearDown(self):
            # Clean up run after every test method.
            pass

    def profile_into(self):
        self.user = Profile(user = 'user')
        self.number = Profile(phone_number = '')
        self.assertTrue(self.user)
        self.assertTrue(self.number)

    def tearDown(self):
        # Clean up run after every test method.
        pass

# class ViewTest(TestCase):
#     def test_setUp(self):
#         self.factory = RequestFactory
#         self.user = User.objects.create_user(username='name', email='user@example.com',  password='password')

    # def test_details(self):
    #     request = self.factory.get('/users/users/profile')
    #     request.user = self.user

#Testing urls.py

class UrlsTest(TestCase):
    client = Client()

    """
    Testing the login of the website:
    Should return an error since we are using Google API to login
    """
    reponse = client.post('/login/', {'email' : 'name@example.com', 'password': 'password'})
    code = reponse.status_code
    print(code)

    """
    testing the profile URL
    """
    response = client.get('profile/')
    response_code = response.content
    print(response_code)

    """
    testing the Questionnaire url
    """
    response = client.get('questionnaire/')
    response_code = response.content
    print(response_code)

    """
    testing the matches URL
    """
    response = client.get('profile/matches/')
    response_code = response.content
    print(response_code)

    """
    testing the friends URL
    """
    response = client.get('profile/friends')
    response_code = response.content
    print(response_code)

    """
    testing the friend request URL
    """
    response = client.get('profile/friends/requests')
    response_code = response.content
    print(response_code)

    """
     testing the Discussion URL
     """
    response = client.get('discussions/')
    response_code = response.content
    print(response_code)

    def tearDown(self):
        # Clean up run after every test method.
        pass

class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='name', email='user@example.com', password='password')


    # def test_profile(self):
    #     request = self.factory.get('profile/')
    #     request.user = self.user
    #     request.user = AnonymousUser()

        # reponse = my_view(request)