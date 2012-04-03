# encoding: utf-8
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

from customers.modelfields import AddressField

# Create your models here.

class Province(models.Model):
    province = models.CharField(_('Province'), max_length=2, primary_key=True)

    def __unicode__(self):
        return self.province

    class Meta:
        ordering = ['province']
        verbose_name = _('Province')
        verbose_name_plural = _('Provinces')

class TownShip(models.Model):
    name = models.CharField(_('Township'), max_length=80)
    province = models.CharField(_('Province'), max_length=2)
    zipcode = models.CharField(_('Zipcode'), max_length=10)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Township')
        verbose_name_plural = _('Townships')
        ordering = ['name', 'zipcode']

class AtecoSector(models.Model):
    code = models.PositiveSmallIntegerField(_('Code'))
    name = models.CharField(_('Name'), unique=True, max_length=200)
    description = models.CharField(_('Description'), max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('ATECO Sector 2007')
        verbose_name_plural = _('ATECO Sectors 2007')

class StandardTask(models.Model):
    name = models.CharField(_('Standard task'), unique=True, max_length=200)
    description = models.CharField(_('Description'), max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Standard task')
        verbose_name_plural = _('Standard tasks')

class Role(models.Model):
    name = models.CharField(_('Role'), unique=True, max_length=200)
    description = models.CharField(_('Description'), max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')

class SecurityDuty(models.Model):
    name = models.CharField(_('Security duty'), unique=True, max_length=200)
    description = models.CharField(_('Description'), max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Security duty')
        verbose_name_plural = _('Security duties')

class Certification(models.Model):
    short_name = models.CharField(_('Short name'), unique=True, max_length=200)
    name = models.CharField(_('Name'), unique=True, max_length=200)
    description = models.CharField(_('Description'), max_length=200)

    class Meta:
        verbose_name = _('Certification')
        verbose_name_plural = _('Certifications')
        unique_together = ('short_name','name')

    def __unicode__(self):
        return self.short_name

class CollaborationAgreement(models.Model):
    name = models.CharField(_('Collaboration Agreement Name'), max_length=200)
    description = models.CharField(_('Description'), max_length=200)

    class Meta:
        verbose_name = _('Collaboration Agreement')
        verbose_name_plural = _('Collaboration Agreements')

    def __unicode__(self):
        return self.name

class Nationality(models.Model):
    nationality = models.CharField(_('Nationality'), max_length=200, unique=True)

    class Meta:
        verbose_name = _('Nationality')
        verbose_name_plural = _('Nationalities')

    def __unicode__(self):
        return self.nationality

class HealthSurveillance(models.Model):
    name = models.CharField(_('Health Surveillance Name'), max_length=200, unique=True)
    description = models.CharField(_('Description'), max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Health surveillance')
        verbose_name_plural = _('Health surveillance')

class CPISettlement(models.Model):
    name = models.CharField(_('CPI Settlement'), max_length=200, unique=True)
    description = models.CharField(_('Description'), max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('CPI Settlement')
        verbose_name_plural = _('CPI Settlements')

class CustomerCompany(models.Model):
    firm = models.CharField(_('Firm'), max_length=200)
    registered_office = AddressField(_('Registered Office'))
    settlement = AddressField(_('Settlement'))
    ciiaa = models.CharField(_('CIIAA registration'), max_length=200, unique=True)
    tax_code = models.CharField(_('Tax code'), max_length=200, unique=True)
    vat_code = models.CharField(_('Vat code'), max_length=200, unique=True)
    inail_pos = models.CharField(_('INAIL position'), max_length=200)
    inps_pos = models.CharField(_('INPS position'), max_length=200)
    ccnl = models.CharField(_('CCNL'), max_length=200)
    ateco_sector = models.ForeignKey(AtecoSector, verbose_name=_('ATECO Sector 2007'))
    certifications = models.ManyToManyField(Certification, verbose_name=_('Certifications'),
                                            null=True, blank=True)
    settlement_size = models.PositiveIntegerField('Settlement size mq.')

    cpi = models.ForeignKey(CPISettlement, verbose_name=_('CPI Settlement'))
    machine_use = models.BooleanField(_('Machine usage'))
    dangerous_substances = models.BooleanField(_('Dangerous substances'))
    health_surveillance = models.BooleanField(_('Health surveillance'))
    phone = models.CharField(_('Phone'), max_length=200)
    fax = models.CharField(_('Fax'), max_length=200)
    email = models.EmailField(_('Email'), max_length=200)
    working_environment = models.TextField(_("Working environment general description"),
                                           null=True, blank=True)
#Descrizione generale dell'ambiente di lavoro
    record_by = models.ForeignKey('accounts.UserProfile',
                                  related_name='companies_created',
                                  verbose_name=_('Recorded by'))
    lastupdate_by = models.ForeignKey('accounts.UserProfile',
                                    related_name='companies_edited',
                                    verbose_name=_('Last update by'))
    record_date = models.DateTimeField(_('Recorded on'), auto_now_add=True)

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
        verbose_name = _('Customer Company')
        verbose_name_plural = _('Customer companies')
        get_latest_by = 'record_date'

class Department(models.Model):
    company = models.ForeignKey(CustomerCompany, verbose_name=_('Customer Company'))
    name = models.CharField(_('Department name'), max_length=200)
    description = models.TextField(_('Department description'))
    size = models.PositiveIntegerField('Department size mq.')

    record_by = models.ForeignKey('accounts.UserProfile',
                                  related_name='departments_created',
                                  verbose_name=_('Recorded by'))
    lastupdate_by = models.ForeignKey('accounts.UserProfile',
                                    related_name='departments_edited',
                                    verbose_name=_('Last update by'))
    record_date = models.DateTimeField(_('Recorded on'), auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')
        unique_together = ('company','name')
        get_latest_by = 'record_date'

    def __unicode__(self):
        return '%s@%s' % (self.name, self.company)

class Staff(models.Model):
    gender_choices = (
        (u'M', _(u'Male')),
        (u'F', _(u'Female')),
        )

    name = models.CharField(_('Name'), max_length=200)
    surname = models.CharField(_('Surname'), max_length=200)
    birth_date = models.DateField(_('Birth date'))
    phone = models.CharField(_('Phone'), max_length=200, null=True, blank=True)
    gender = models.CharField(_('Gender'), max_length=2, choices=gender_choices)
    nationality = models.ForeignKey(Nationality,
                                    verbose_name=_('Nationality'))
    collagreement = models.ForeignKey(CollaborationAgreement,
                                      verbose_name=_('Collaboration agreement'))
#    health_surveillance = models.ManyToManyField(HealthSurveillance, verbose_name=_('Sorveglianza Sanitaria'))
    health_surveillance = models.BooleanField(_('Health surveillance'))
    workers_count = models.BooleanField(_('Workers count'))

    company = models.ForeignKey(CustomerCompany, null=False, verbose_name=_('Customer Company'))
    standard_task = models.ForeignKey(StandardTask, null=False, verbose_name=_('Standard task'))
    department = models.ForeignKey(Department, null=False, verbose_name=_('Department'))
    role = models.ForeignKey(Role, null=False, verbose_name=_('Role'))
    employ_date = models.DateField(verbose_name=_('Employ date'), null=True, blank=True)

    record_by = models.ForeignKey('accounts.UserProfile',
                                  related_name='staff_created',
                                  verbose_name=_('Recorded by'))
    lastupdate_by = models.ForeignKey('accounts.UserProfile',
                                    related_name='staff_edited',
                                    verbose_name=_('Last update by'))
    record_date = models.DateTimeField(_('Recorded on'), auto_now_add=True)

    def __unicode__(self):
        return u'%s %s' % (self.surname, self.name) # mansione omogenea

    class Meta:
        ordering = ['surname','name']
        verbose_name = _('Staff')
        verbose_name_plural = _('Staff')
        unique_together = ('surname','name', 'birth_date')

class CompanySecurityDuty(models.Model):
    company = models.ForeignKey(CustomerCompany, verbose_name=_('Customer Company'))
    security_duty = models.ForeignKey(SecurityDuty, verbose_name=_('Security duty'))
    surname = models.CharField(_('Surname'), max_length=200)
    name = models.CharField(_('Name'), max_length=200)
    internal_phone = models.CharField(_('Internal phone'), max_length=200, null=True, blank=True)
    external_phone = models.CharField(_('External phone'), max_length=200, null=True, blank=True)
    email = models.EmailField(_('Email'), max_length=200)

    record_by = models.ForeignKey('accounts.UserProfile',
                                  related_name='secduty_created',
                                  verbose_name=_('Recorded by'))
    lastupdate_by = models.ForeignKey('accounts.UserProfile',
                                    related_name='secduty_edited',
                                    verbose_name=_('Last update by'))
    record_date = models.DateTimeField(_('Recorded on'), auto_now_add=True)

    def __unicode__(self):
        return u'%s %s (%s)' % (self.surname, self.name, self.security_duty)

    class Meta:
        verbose_name = _('Company security duty')
        verbose_name_plural = _('Company security duties')

class Machine(models.Model):
    department = models.ForeignKey(Department, null=False, verbose_name=_('Department'))
    code = models.CharField(_('Code'), max_length=200)
    description = models.TextField(_('Description'), blank=True, null=True)
