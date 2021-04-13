from django.contrib.auth import get_user_model
from django.test import TestCase
from django.contrib.auth.models import  User
from .models import Profile
# from .models import DormChoice
# from .models import SchoolChoice


# Create your tests here.

class CreateProfileTest(TestCase):
    """
    Prints that you can continue making your account if a name has been entered
    """

    def setUp_with_name(self):
        User = get_user_model()
        new_user = User.objects.create_user(user="new_user", name="user")
        #create_name = User.objects.create(name="Sarah")
        self.assertEqual(new_user.user, "new_user")
        self.assertEqual(new_user.name, "user")
        print("You can save your account")


    def profile_is_unique(self):
        new_user = User.objects.create_user(user="new_user", name="user")
        self.assertEqual(new_user.profile, Profile.objects.get(user=new_user))
        print("You can continue creating an account as you have made an email")

    def test_assert(self):
        self.assertTrue(True)

    def tes_seert(self):
        self.assertFalse(True)







