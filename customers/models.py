# encoding: utf-8
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class AtecoSector(models.Model):
    name = models.CharField('Nome', max_length=200)
    description = models.CharField('Descrizione', max_length=200)

    def __unicode__(self):
        return self.name

class StandardTask(models.Model):
    name = models.CharField('Mansione omogenea', max_length=200)
    description = models.CharField('Descrizione', max_length=200)

    def __unicode__(self):
        return self.name

class Role(models.Model):
    name = models.CharField('Mansione', max_length=200)
    description = models.CharField('Descrizione', max_length=200)

    def __unicode__(self):
        return self.name

class SecurityDuty(models.Model):
    name = models.CharField('Figura prevenzione', max_length=200)
    description = models.CharField('Descrizione', max_length=200)

    def __unicode__(self):
        return self.name

class Certification(models.Model):
    short_name = models.CharField('Sigla', max_length=200)
    name = models.CharField('Nome', max_length=200)
    description = models.CharField('Descrizione', max_length=200)

    def __unicode__(self):
        return self.short_name

class Department(models.Model):
    name = models.CharField('Nome reparto', max_length=200)
    description = models.CharField('Descrizione', max_length=200)

    def __unicode__(self):
        return self.name

class Staff(models.Model):
    gender_choices = (
        (u'M', u'Maschio'),
        (u'F', u'Femmina'),
        )

    name = models.CharField('Nome', max_length=200)
    surname = models.CharField('Cognome', max_length=200)
    birth_date = models.DateField('Data di nascita')
    phone = models.CharField('Telefono', max_length=200)
    gender = models.CharField('Sesso', max_length=2, choices=gender_choices)
    nationality = models.CharField("Nazionalità", max_length=200)
    collagreement = models.CharField('Forma contrattuale', max_length=200)
    health_care = models.CharField('Sorveglianza sanitaria', max_length=200)
    workers_count = models.BooleanField('Computo lavoratori')

    standard_task = models.ManyToManyField(StandardTask, through='Employ',
                                    verbose_name='Mansione Omogenea')

    def __unicode__(self):
        return u'%s %s' % (self.surname, self.name) # mansione omogenea

class CustomerCompany(models.Model):
    firm = models.CharField('Ragione sociale', max_length=200)
    registered_office = models.CharField('Sede legale amministrativa',
                                                  max_length=200)
    settlement = models.CharField('Sede insediamento produttivo',
                                                    max_length=200)
    ciiaa = models.CharField('Iscrizione CIIAA', max_length=200)
    tax_code = models.CharField('Codice fiscale', max_length=200)
    vat_code = models.CharField('Partita IVA', max_length=200)
    inail_pos = models.CharField('Posizione INAIL', max_length=200)
    inps_pos = models.CharField('Posizione INPS', max_length=200)
    ccnl = models.CharField('CCNL', max_length=200)
    ateco_sector = models.OneToOneField(AtecoSector, verbose_name='Settore Ateco 2007')
    certifications = models.ManyToManyField(Certification, verbose_name='Certificazioni')
    settlement_size = models.CharField(max_length=200)
    record_date = models.DateTimeField('Data registrazione')
    cpi = models.CharField('CPI', max_length=200)
    machine_use = models.BooleanField('Uso macchine')
    dangerous_substances = models.BooleanField('Sostanze pericolose')
    health_surveillance = models.BooleanField('Sorveglianza sanitaria')
    phone = models.CharField(max_length=200)
    fax = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    employes = models.ManyToManyField(Staff, through='Employ')
    
    def __unicode__(self):
        return self.firm

class Employ(models.Model):
    company = models.ForeignKey(CustomerCompany, null=False)
    staff = models.ForeignKey(Staff, primary_key=True)
    standard_task = models.ForeignKey(StandardTask, null=False)
    role = models.ForeignKey(Role, null=False)
    security_duty = models.ForeignKey(SecurityDuty, null=True)
    date = models.DateField(auto_now_add=True)
