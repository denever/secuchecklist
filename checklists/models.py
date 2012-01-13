from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Checklist(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField('Creation date')
    
    def __unicode__(self):
        return self.title

class Check(models.Model):
    answertypes = (
        ('BO', 'Boolean check'),
        ('MC', 'Multiple check'),
        ('PC', 'Percentage check'),
        )
    
    checklist = models.ForeignKey(Checklist)
    descr = models.CharField(max_length=200)
    answertype = models.CharField(max_length=2, choices=answertypes)

    def __unicode__(self):
        return self.descr

class BooleanCheckResult(models.Model):
    check = models.ForeignKey(Check)
    value = models.BooleanField()

    def __unicode__(self):
        return self.check.descr

class MultipleCheckResult(models.Model):
    check = models.ForeignKey(Check)
    values = models.CommaSeparatedIntegerField(max_length=20)

    def __unicode__(self):
        return self.check.descr

def validate_percentage(value):
    if value < 0 or value > 100:
        raise ValidationError(u'%s out of range')

class PercentageCheckResult(models.Model):
    check = models.ForeignKey(Check)
    value = models.SmallIntegerField(validators=[validate_percentage])

    def __unicode__(self):
        return self.check.descr
