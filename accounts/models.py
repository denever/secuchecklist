# encoding: utf-8
from django.db import models

# importing User for UserProfile
from django.contrib.auth.models import User

# importing for signals and logging
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils.encoding import force_unicode
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

LOGIN, LOGOUT, CREATE, EDIT, DELETE = 'Logged In', 'Logged Out', 'Created', 'Edited', 'Deleted'

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
    instance = kwargs['instance']
    if hasattr(instance, 'record_by'):
        a = Activity(userprofile=instance.record_by if kwargs['created'] else instance.lastupdate_by,
                     action=CREATE if kwargs['created'] else EDIT,
                     object_repr=force_unicode(instance),
                     content_object=instance
                     )
        a.save()

@receiver(post_delete)
def post_delete_cb(sender, **kwargs):
    instance = kwargs['instance']
    if hasattr(instance, 'record_by'):
        a = Activity(userprofile = instance.record_by,
                     action = DELETE,
                     object_repr = force_unicode(instance),
                     content_object = instance
                     )
        a.save()

@receiver(user_logged_in)
def logged_in_cb(sender, **kwargs):
    user_profile = kwargs['user'].get_profile()
    a = Activity(userprofile = user_profile,
                 action = LOGIN,
                 object_repr = force_unicode(user_profile),
                 content_object = user_profile
                 )
    a.save()


@receiver(user_logged_out)
def logged_out_cb(sender, **kwargs):
    user_profile = kwargs['user'].get_profile()
    a = Activity(userprofile = user_profile,
                 action = LOGOUT,
                 object_repr = force_unicode(user_profile),
                 content_object = user_profile
                 )
    a.save()
