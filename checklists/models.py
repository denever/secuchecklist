from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Checklist(models.Model):
    title = models.CharField(max_length=200)
    creation_date = models.DateTimeField('Creation date')
    expire_date = models.DateTimeField('Expire date')
    active = models.BooleanField()

    def __unicode__(self):
        return self.title

class BooleanCheck(models.Model):
    checklist = models.ForeignKey(Checklist)
    descr = models.CharField(max_length=200)

    def __unicode__(self):
        return self.descr

class SingleCheck(models.Model):
    checklist = models.ForeignKey(Checklist)
    descr = models.CharField(max_length=200)

    def __unicode__(self):
        return self.descr

class SingleChoice(models.Model):
    singlecheck = models.ForeignKey(SingleCheck)
    descr = models.CharField(max_length=200)
    value = models.IntegerField()

class MultipleCheck(models.Model):
    checklist = models.ForeignKey(Checklist)
    descr = models.CharField(max_length=200)

    def __unicode__(self):
        return self.descr

class MultipleChoice(models.Model):
    multiplecheck = models.ForeignKey(MultipleCheck)
    descr = models.CharField(max_length=200)
    value = models.IntegerField()

class NumericCheck(models.Model):
    checklist = models.ForeignKey(Checklist)
    descr = models.CharField(max_length=200)
    minvalue = models.IntegerField()
    maxvalue = models.IntegerField()

    def __unicode__(self):
        return self.descr

class Customer(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    piva = models.CharField(max_length=200)

class ChecklistResult(models.Model):
    checklist = models.ForeignKey(Checklist)
    customer = models.ForeignKey(Customer)

class BooleanCheckResult(models.Model):
    checklistresult = models.ForeignKey(ChecklistResult)
    value = models.BooleanField()

class SingleCheckResult(models.Model):
    checklistresult = models.ForeignKey(ChecklistResult)
    value = models.IntegerField()

class MultipleCheckResult(models.Model):
    checklistresult = models.ForeignKey(ChecklistResult)
    values = models.CommaSeparatedIntegerField(max_length=200)

class NumericCheckResult(models.Model):
    checklistresult = models.ForeignKey(ChecklistResult)
    value = models.IntegerField()
