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

    class Meta:
        verbose_name_plural = 'SecurityDuties'        

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
    ateco_sector = models.ForeignKey(AtecoSector, verbose_name='Settore Ateco 2007')
    certifications = models.ManyToManyField(Certification, verbose_name='Certificazioni')
    settlement_size = models.CharField('Superficie insediamento', max_length=200)
    record_date = models.DateTimeField('Data registrazione', auto_now_add=True)
    cpi = models.CharField('CPI', max_length=200)
    machine_use = models.BooleanField('Uso macchine')
    dangerous_substances = models.BooleanField('Sostanze pericolose')
    health_surveillance = models.BooleanField('Sorveglianza sanitaria')
    phone = models.CharField('Telefono', max_length=200)
    fax = models.CharField('Fax', max_length=200)
    email = models.EmailField('Email', max_length=200)

    def departments(self):
        return list(set([staff.department for staff in self.staff_set.all()]))

    def standard_tasks(self):
        return list(set([staff.standard_task for staff in self.staff_set.all()]))

    def roles(self):
        return list(set([staff.role for staff in self.staff_set.all()]))

    def security_duties(self):
        return list(set([staff.security_duty for staff in self.staff_set.all()]))

    def workers_count(self):
        return self.staff_set.filter(workers_count=True).count()

    def __unicode__(self):
        return self.firm

    class Meta:
        ordering = ['-record_date']
        verbose_name_plural = 'CustomerCompanies'
        get_latest_by = 'record_date'

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

    company = models.ForeignKey(CustomerCompany, null=False, verbose_name='Azienda')
    standard_task = models.ForeignKey(StandardTask, null=False, verbose_name='Mansione Omogenea')
    department = models.ForeignKey(Department, null=False, verbose_name='Reparto')
    role = models.ForeignKey(Role, null=False, verbose_name='Mansione')
    security_duty = models.ForeignKey(SecurityDuty, null=True, verbose_name='Figura Prevenzione')
    date = models.DateField(verbose_name='Data assunzione')

    def __unicode__(self):
        return u'%s %s' % (self.surname, self.name) # mansione omogenea

    class Meta:
        ordering = ['surname','name']
