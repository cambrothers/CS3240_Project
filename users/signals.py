from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile,Relation

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
   if created:
     Profile.objects.create(user=instance)

@receiver(post_save,sender=Relation)
def add_to_friends(sender,created,instance,**kwargs):
    sender_ = instance.sender.user
    print(sender_)
    receiver_= instance.receiver.user
    print(receiver_)
    if instance.status == 'accepted':
        print("hi")
        sender_.friends.add(receiver_)
        receiver_.friends.add(sender_)
        sender_.save()
        receiver_.save()

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()
