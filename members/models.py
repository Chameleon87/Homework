from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class Member(models.Model):
    user        = models.OneToOneField(User)
    email       = models.EmailField()
    
    def __unicode__(self):
        return self.name
    
def create_member_user_callback(sender, instance, **kwargs):
    member, new = Member.objects.get_or_create(user=instance)
post_save.connect(create_member_user_callback, User)