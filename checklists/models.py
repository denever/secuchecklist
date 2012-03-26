from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class RiskFactor(models.Model):
    description = models.CharField('Descrizione', max_length=200, null=True, blank=True)
    question = models.TextField('Domanda', null=True, blank=True)
    measure = models.TextField('Misura', null=True, blank=True)
    suggestion_yes = models.TextField('Suggerimento Si', null=True, blank=True)
    suggestion_no = models.TextField('Suggerimento No', null=True, blank=True)
    notes = models.TextField('Note', null=True, blank=True)
    link = models.CharField('Link', max_length=200, null=True, blank=True)
    filename = models.FileField('Filename', null=True, blank=True, upload_to='riskfactor_attaches')
    belongs_to = models.ForeignKey('self', null=True, blank=True, verbose_name="Padre")

    record_date = models.DateTimeField('Data inserimento', auto_now_add=True)

    codice = models.CharField('Codice', max_length=200, null=True, blank=True, unique=True)
    codice_padre = models.CharField('Codice Padre', max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.description
