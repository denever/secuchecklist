# encoding: utf-8
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class SettoreAteco(models.Model):
    titolo = models.CharField(max_length=200)
    descrizione = models.CharField(max_length=200)

    def __unicode__(self):
        return self.titolo

class MansioneOmogenea(models.Model):
    titolo = models.CharField(max_length=200)
    descrizione = models.CharField(max_length=200)

    def __unicode__(self):
        return self.titolo

class FiguraPrevenzione(models.Model):
    titolo = models.CharField(max_length=200)
    descrizione = models.CharField(max_length=200)

    def __unicode__(self):
        return self.titolo

class Certificazione(models.Model):
    sigla = models.CharField(max_length=200)
    descrizione = models.CharField(max_length=200)

    def __unicode__(self):
        return self.sigla

class ResultChecklistGenerica(models.Model):
    nome = models.CharField(max_length=200)
    data_compilazione = models.DateTimeField('Data registrazione')
    data_modifica = models.DateTimeField('Data registrazione')
    descrizione = models.CharField(max_length=200)

    def __unicode__(self):
        return '%s (%s)' % (self.nome, self.data_compilazione)

class ResultChecklistReparto(models.Model):
    nome = models.CharField(max_length=200)
    data_compilazione = models.DateTimeField('Data compilazione')
    data_modifica = models.DateTimeField('Data modifica')
    descrizione = models.CharField(max_length=200)

    def __unicode__(self):
        return '%s (%s)' % (self.nome, self.data_compilazione)

class ResultChecklistMansioneOmogenea(models.Model):
    nome = models.CharField(max_length=200)
    data_compilazione = models.DateTimeField('Data compilazione')
    data_modifica = models.DateTimeField('Data modifica')
    descrizione = models.CharField(max_length=200)

    def __unicode__(self):
        return '%s (%s)' % (self.nome, self.data_compilazione)

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
    settore_ateco = models.ForeignKey(SettoreAteco, verbose_name='Settore Ateco 2007')
    certificazioni = models.ManyToManyField(Certificazione)
    superficie_insediamento = models.CharField(max_length=200)
    data_registrazione = models.DateTimeField('Data registrazione')
    cpi = models.CharField('CPI', max_length=200)
    uso_macchine = models.BooleanField()
    sostanze_pericolose = models.BooleanField()
    sorveglianza_sanitaria = models.BooleanField()
    telefono = models.CharField(max_length=200)
    fax = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    checklist_generiche = models.ManyToManyField(ResultChecklistGenerica)
    checklist_reparti = models.ManyToManyField(ResultChecklistReparto)
    checklist_mansioni = models.ManyToManyField(ResultChecklistMansioneOmogenea)

    def __unicode__(self):
        return self.ragione_sociale

class Reparto(models.Model):
    azienda = models.ForeignKey(Azienda)
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
    reparto = models.ManyToManyField(Reparto)
    nazionalita = models.CharField("Nazionalità", max_length=200)
    forma_contrattuale = models.CharField(max_length=200)
    sorveglianza_sanitaria = models.CharField(max_length=200)
    computo_lavoratori = models.BooleanField()

    def __unicode__(self):
        return u'%s %s (%s)' % (self.cognome, self.nome, self.mansione_omogenea)

class FigureAziendaPrevenzione(models.Model):
    azienda = models.ForeignKey(Azienda)
    figura = models.ForeignKey(FiguraPrevenzione)
    nome = models.CharField(max_length=200)
    cognome = models.CharField(max_length=200)
    data_nascita = models.DateField('Data registrazione')
    telefono = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s %s (%s)' % (self.cognome, self.nome, self.figura)
