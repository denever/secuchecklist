from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    # checklist suspendend
    # checklist completed
    # customercompany_set tutte le compagnie da te registrate

    def __unicode__(self):
        return self.user.username
    
