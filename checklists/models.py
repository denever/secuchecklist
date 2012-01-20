# encoding: utf-8
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class SettoreAteco(models.Model):
    titolo = models.CharField(max_length=200)
    descrizione = models.CharField(max_length=200)

    def __unicode__(self):
        return self.titolo

class Azienda(models.Model):
    ragione_sociale = models.CharField(max_length=200)
    sede_legale_amministrativa = models.CharField(max_length=200)
    sede_insediamento_produttivo = models.CharField(max_length=200)
    iscrizione_ciiaa = models.CharField('Iscrizione CIIAA', max_length=200)
    codice_fiscale = models.CharField(max_length=200)
    partita_iva = models.CharField('Partita IVA', max_length=200)
    posizione_inail = models.CharField('Posizione INAIL', max_length=200)
    posizione_inps = models.CharField('Posizione INPS', max_length=200)
    ccnl = models.CharField('CCNL', max_length=200)
    settore_ateco = models.ForeignKey(SettoreAteco)
    certificazioni = models.CharField(max_length=200)
    superficie_insediamento = models.CharField(max_length=200)
    data_registrazione = models.DateTimeField('Data registrazione')
    cpi = models.CharField('CPI', max_length=200)
    uso_macchine = models.BooleanField()
    sostanze_pericolose = models.BooleanField()
    sorveglianza_sanitaria = models.BooleanField()
    telefono = models.CharField(max_length=200)
    fax = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __unicode__(self):
        return self.ragione_sociale

class MansioneOmogenea(models.Model):
    titolo = models.CharField(max_length=200)
    descrizione = models.CharField(max_length=200)

    def __unicode__(self):
        return self.titolo

class Lavoratore(models.Model):
    gender_choices = (
        (u'M', u'Maschio'),
        (u'F', u'Femmina'),
        )
    azienda = models.ForeignKey(Azienda)
    nome = models.CharField(max_length=200)
    cognome = models.CharField(max_length=200)
    data_nascita = models.DateField('Data di nascita')
    sesso = models.CharField(max_length=2, choices=gender_choices)
    mansione = models.CharField(max_length=200)
    mansione_omogenea = models.ForeignKey(MansioneOmogenea)
    reparto = models.CharField(max_length=200)
    nazionalita = models.CharField("Nazionalità", max_length=200)
    forma_contrattuale = models.CharField(max_length=200)
    sorveglianza_sanitaria = models.CharField(max_length=200)
    computo_lavoratori = models.BooleanField()

    def __unicode__(self):
        return u'%s %s (%s)' % (self.cognome, self.nome, self.mansione_omogenea)

class FiguraPrevenzione(models.Model):
    titolo = models.CharField(max_length=200)
    descrizione = models.CharField(max_length=200)

    def __unicode__(self):
        return self.titolo

class FigureAziendaPrevenzione(models.Model):
    azienda = models.ForeignKey(Azienda)
    figura = models.ForeignKey(FiguraPrevenzione)
    nome = models.CharField(max_length=200)
    cognome = models.CharField(max_length=200)
    data_nascita = models.DateField('Data registrazione')
    telefono = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s %s (%s)' % (self.cognome, self.nome, self.figura)
