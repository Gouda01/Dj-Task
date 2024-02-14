from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class Profile (models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile',default='profile/default.png')
    about = models.CharField(max_length=1000)
    facebook = models.CharField(max_length=200,blank=True,null=True)
    twitter = models.CharField(max_length=200,blank=True,null=True)
    linkedin = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return str(self.user)



@receiver(post_save,sender=User)
def create_profile(sender, instance, created, **kwargs ):
    if created :
        Profile.objects.create (
            user = instance
        )