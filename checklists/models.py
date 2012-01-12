from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Checklist(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField('date')

class Check(models.Model):
    checklist = models.ForeignKey(Checklist)
    descr = models.CharField(max_length=200)
    answertype = models.CharField(max_length=200)

class BooleanCheckResult(models.Model):
    check = models.ForeignKey(Check)
    value = models.BooleanField()

class MultipleCheckResult(models.Model):
    check = models.ForeignKey(Check)
    values = models.CommaSeparatedIntegerField(max_length=20)

def validate_percentage(value):
    if value < 0 or value > 100:
        raise ValidationError(u'%s out of range')

class PercentageCheckResult(models.Model):
    check = models.ForeignKey(Check)
    value = models.SmallIntegerField(validators=[validate_percentage])
