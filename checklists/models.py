from django.db import models
from django.core.execptions import ValidationError

# Create your models here.

class CheckList(models.Model):
    title = models.CharField(max_lenghth=200)
    date = models.DateTimeField('date')

class BooleanCheck(models.Model):
    checklist = models.ForeignKey(CheckList)
    descr = models.CharField(max_length=200)
    value = models.BooleanField()

class MultipleCheck(models.Model):
    checklist = models.ForeignKey(CheckList)
    descr = models.CharField(max_length=200)
    values = models.CommaSeparatedIntegerField(max_length=20)

def validate_percentage(value):
    if value < 0 or value > 100:
        raise ValidationError(u'%s out of range')

class PercentageCheck(models.Model):
    checklist = models.ForeignKey(CheckList)
    descr = models.CharField(max_length=200)
    value = models.SmallIntegerField(validators=[validate_percentage])

