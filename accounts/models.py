# encoding: utf-8
from django.db import models

# importing User for UserProfile
from django.contrib.auth.models import User

# importing for signals and logging
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.encoding import force_unicode
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

CREATE, EDIT, DELETE = 'Create', 'Edit', 'Delete'

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    # checklist suspendend
    # checklist completed
    # customercompany_set tutte le compagnie da te registrate

    def __unicode__(self):
        return self.user.username

class Activity(models.Model):
    userprofile = models.ForeignKey(UserProfile)
    date = models.DateTimeField('Data attività', auto_now_add=True)
    action = models.CharField('Attività', max_length=6)
    object_id = models.PositiveIntegerField()
    object_repr = models.CharField('Nome Oggetto', max_length=50)
    content_type = models.ForeignKey(ContentType)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return '%s %s %s %s' % (self.date, self.userprofile, self.action, self.object_repr)

@receiver(post_save)
def post_save_cb(sender, **kwargs):
    print sender
    print kwargs
    instance = kwargs['instance']
    if hasattr(instance, 'record_by'):
        a = Activity(userprofile=instance.record_by,
                     action=CREATE,
                     object_repr=force_unicode(instance),
                     content_object=instance
                     )
        a.save()

@receiver(post_delete)
def post_delete_cb(sender, **kwargs):
    print sender
    print kwargs
    instance = kwargs['instance']
    if hasattr(instance, 'record_by'):
        a = Activity(userprofile = instance.record_by,
                     action = DELETE,
                     object_repr = force_unicode(instance),
                     content_object = instance
                     )
        a.save()
