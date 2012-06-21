# encoding: utf-8
from django.db import models
from django.utils.translation import ugettext as _

# importing User for UserProfile
from django.contrib.auth.models import User

# importing for signals and logging
from django.db.models.signals import pre_save, post_save, pre_delete
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils.encoding import force_unicode
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils import simplejson

from customers.models import CustomerCompany, Department, Staff, CompanySecurityDuty, Equipment
from risksevaluation.models import RisksEvaluationDocument

LOGIN, LOGOUT, CREATE, EDIT, DELETE = range(5)

actions = [_('Logged In'), _('Logged Out'), _('Created'), _('Edited'), _('Deleted')]

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    # Risks Evaluation Documents suspendend
    # Risks Evaluation Documents completed
    # customercompany_set tutte le compagnie da te registrate

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Account')

class Activity(models.Model):
    userprofile = models.ForeignKey(UserProfile)
    date = models.DateTimeField(_('Activity date'), auto_now_add=True)
    action = models.PositiveSmallIntegerField(_('Action'))
    object_id = models.PositiveIntegerField()
    object_repr = models.CharField(_('Object name'), max_length=50)
    content_type = models.ForeignKey(ContentType)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    in_revision = models.ForeignKey(RisksEvaluationDocument, blank=True, null=True)
    serialized_data = models.TextField(help_text="The serialized form of this version of the model.")

    class Meta:
        ordering = ['-date']
        verbose_name = _('Activity')
        verbose_name_plural = _('Activities')

    def __unicode__(self):
        return '%s %s %s %s' % (self.date, self.userprofile, self.action, self.object_repr)

    def get_action_description(self):
        return actions[self.action]

    def get_content_type_name(self):
        return self.content_type.model_class()._meta.verbose_name

@receiver(pre_save)
def pre_save_cb(sender, **kwargs):
    if sender in (CustomerCompany, Department, Staff, CompanySecurityDuty, Equipment):
        customers_pre_save_cb(sender, **kwargs)
    else:
        print '#'*10, 'Pre save', sender

def customers_pre_save_cb(sender, **kwargs):
    instance = kwargs['instance']
    try:
        diff = dict()
        old_instance = instance.__class__._default_manager.filter(pk=instance.pk).get()
        for field in old_instance._meta.fields:
            if getattr(old_instance, field.attname) != getattr(instance, field.attname):
                diff[field.verbose_name] = {'old_value': unicode(getattr(old_instance, field.attname)),
                                            'new_value': unicode(getattr(instance, field.attname))}
        a = Activity(userprofile=instance.lastupdate_by,
                     action=EDIT,
                     object_repr=force_unicode(instance),
                     content_object=instance,
                     serialized_data=simplejson.dumps(diff)
        )
        a.save()
    except Exception, e:
        print e

@receiver(post_save)
def post_save_cb(sender, **kwargs):
    if sender in (CustomerCompany, Department, Staff, CompanySecurityDuty, Equipment):
        customers_post_save_cb(sender, **kwargs)
    else:
        print '#'*10, 'Save', sender

def customers_post_save_cb(sender, **kwargs):
    instance = kwargs['instance']
    if kwargs['created'] and hasattr(instance, 'record_by'):
        diff = dict()
        for field in instance._meta.fields:
            diff[field.verbose_name] = {'old_value': None,
                                        'new_value': unicode(getattr(instance, field.attname))}

        a = Activity(userprofile=instance.record_by,
                     action=CREATE,
                     object_repr=force_unicode(instance),
                     content_object=instance,
                     serialized_data=simplejson.dumps(diff)
        )
        a.save()

@receiver(pre_delete)
def pre_delete_cb(sender, **kwargs):
    if sender in (CustomerCompany, Department, Staff, CompanySecurityDuty, Equipment):
        customers_pre_delete_cb(sender, **kwargs)
    else:
        print '#'*10, 'Save', sender


def customers_pre_delete_cb(sender, **kwargs):
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
