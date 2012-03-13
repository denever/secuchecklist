# encoding: utf-8
from django.db import models
from django.core.exceptions import ValidationError

from customers.modelfields import AddressField

# Create your models here.

class AtecoSector(models.Model):
    name = models.CharField('Nome', unique=True, max_length=200)
    description = models.CharField('Descrizione', max_length=200)

    def __unicode__(self):
        return self.name

class StandardTask(models.Model):
    name = models.CharField('Mansione omogenea', unique=True, max_length=200)
    description = models.CharField('Descrizione', max_length=200)

    def __unicode__(self):
        return self.name

class Role(models.Model):
    name = models.CharField('Mansione', unique=True, max_length=200)
    description = models.CharField('Descrizione', max_length=200)

    def __unicode__(self):
        return self.name

class SecurityDuty(models.Model):
    name = models.CharField('Figura prevenzione', unique=True, max_length=200)
    description = models.CharField('Descrizione', max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'SecurityDuties'

class Certification(models.Model):
    short_name = models.CharField('Sigla', unique=True, max_length=200)
    name = models.CharField('Nome', unique=True, max_length=200)
    description = models.CharField('Descrizione', max_length=200)

    class Meta:
        unique_together = ('short_name','name')

    def __unicode__(self):
        return self.short_name

class CollaborationAgreement(models.Model):
    name = models.CharField('Nome forma contrattuale', max_length=200)
    description = models.CharField('Descrizione', max_length=200)

    class Meta:
        verbose_name = 'Forma Contrattuale'
        verbose_name_plural = 'Forme Contrattuali'

    def __unicode__(self):
        return self.name

class Nationality(models.Model):
    nationality = models.CharField("Nazionalità", max_length=200, unique=True)

    class Meta:
        verbose_name_plural = 'Nationalities'

    def __unicode__(self):
        return self.nationality

class HealthSurveillance(models.Model):
    name = models.CharField('Nome sorveglianza sanitaria', max_length=200, unique=True)
    description = models.CharField('Descrizione', max_length=200)

    def __unicode__(self):
        return self.name

class CPISettlement(models.Model):
    name = models.CharField('Insediamento CPI', max_length=200, unique=True)
    description = models.CharField('Descrizione', max_length=200)

    def __unicode__(self):
        return self.name

class CustomerCompany(models.Model):
    firm = models.CharField('Ragione sociale', max_length=200)
    registered_office = AddressField('Sede legale amministrativa')
    settlement = AddressField('Sede insediamento produttivo')
    ciiaa = models.CharField('Iscrizione CIIAA', max_length=200, unique=True)
    tax_code = models.CharField('Codice fiscale', max_length=200, unique=True)
    vat_code = models.CharField('Partita IVA', max_length=200, unique=True)
    inail_pos = models.CharField('Posizione INAIL', max_length=200)
    inps_pos = models.CharField('Posizione INPS', max_length=200)
    ccnl = models.CharField('CCNL', max_length=200)
    ateco_sector = models.ForeignKey(AtecoSector, verbose_name='Settore Ateco 2007')
    certifications = models.ManyToManyField(Certification, verbose_name='Certificazioni',
                                            null=True, blank=True)
    settlement_size = models.PositiveIntegerField('Superficie insediamento mq.')

    cpi = models.ForeignKey(CPISettlement, verbose_name='Insediamento CPI')
    machine_use = models.BooleanField('Uso macchine')
    dangerous_substances = models.BooleanField('Sostanze pericolose')
    health_surveillance = models.BooleanField('Sorveglianza sanitaria')
    phone = models.CharField('Telefono', max_length=200)
    fax = models.CharField('Fax', max_length=200)
    email = models.EmailField('Email', max_length=200)
    working_environment = models.TextField("Descrizione generale dell'ambiente di lavoro",
                                           null=True, blank=True)

    record_by = models.ForeignKey('accounts.UserProfile', verbose_name='Assegnata a')
    record_date = models.DateTimeField('Data registrazione', auto_now_add=True)

    # def departments(self):
    #     return list(set([staff.department for staff in self.staff_set.all()]))

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
        ordering = ['record_date']
        verbose_name_plural = 'CustomerCompanies'
        get_latest_by = 'record_date'

class Department(models.Model):
    company = models.ForeignKey(CustomerCompany, verbose_name='Azienda')
    name = models.CharField('Nome reparto', max_length=200)
    description = models.TextField('Descrizione del reparto')
    size = models.PositiveIntegerField('Superficie mq.')

    record_by = models.ForeignKey('accounts.UserProfile', verbose_name='Assegnata a')
    record_date = models.DateTimeField('Data registrazione', auto_now_add=True)

    class Meta:
        ordering = ['name']
        unique_together = ('company','name')
        get_latest_by = 'record_date'

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
    phone = models.CharField('Telefono', max_length=200, null=True, blank=True)
    gender = models.CharField('Sesso', max_length=2, choices=gender_choices)
    nationality = models.ForeignKey(Nationality,
                                    verbose_name='Nazionalità')
    collagreement = models.ForeignKey(CollaborationAgreement,
                                      verbose_name='Forma Contrattuale')
    health_surveillance = models.ManyToManyField(HealthSurveillance, verbose_name='Sorveglianza Sanitaria')
    workers_count = models.BooleanField('Computo lavoratori')

    company = models.ForeignKey(CustomerCompany, null=False, verbose_name='Azienda')
    standard_task = models.ForeignKey(StandardTask, null=False, verbose_name='Mansione Omogenea')
    department = models.ForeignKey(Department, null=False, verbose_name='Reparto')
    role = models.ForeignKey(Role, null=False, verbose_name='Mansione')
    employ_date = models.DateField(verbose_name='Data assunzione', null=True, blank=True)

    record_by = models.ForeignKey('accounts.UserProfile', verbose_name='Assegnata a')
    record_date = models.DateTimeField('Data registrazione', auto_now_add=True)

    def __unicode__(self):
        return u'%s %s' % (self.surname, self.name) # mansione omogenea

    class Meta:
        ordering = ['surname','name']
        unique_together = ('surname','name', 'birth_date')

class CompanySecurityDuty(models.Model):
    company = models.ForeignKey(CustomerCompany, verbose_name='Azienda')
    security_duty = models.ForeignKey(SecurityDuty, verbose_name='Figura Prevenzione')
    surname = models.CharField('Cognome', max_length=200)
    name = models.CharField('Nome', max_length=200)
    internal_phone = models.CharField('Telefono interno', max_length=200, null=True, blank=True)
    external_phone = models.CharField('Telefono esterno', max_length=200, null=True, blank=True)
    email = models.EmailField('Email', max_length=200)

    record_by = models.ForeignKey('accounts.UserProfile', verbose_name='Assegnata a')
    record_date = models.DateTimeField('Data registrazione', auto_now_add=True)

    def __unicode__(self):
        return u'%s %s (%s)' % (self.surname, self.name, self.security_duty)

    class Meta:
        verbose_name_plural = 'CompanySecurityDuties'
