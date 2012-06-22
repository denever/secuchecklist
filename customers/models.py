# encoding: utf-8
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q

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
    year_beginactivity = models.IntegerField(_('Year activity begins'), null=True, blank=True)
    ateco_sector = models.ForeignKey(AtecoSector, verbose_name=_('ATECO Sector 2007'))
    certifications = models.ManyToManyField(Certification, verbose_name=_('Certifications'),
                                            null=True, blank=True)
    settlement_size = models.PositiveIntegerField(_('Settlement size mq.'))

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

    newrevision_needed = models.BooleanField(_('New Revision Needed'), default=True)

    def standard_tasks(self):
        return list(set([staff.standard_task for staff in self.staff_set.all()]))

    def roles(self):
        return list(set([staff.role for staff in self.staff_set.all()]))

    def equipments(self, fieldname=None):
        equips = list()
        if fieldname:
            for dep in self.department_set.all():
                equips.extend([value[fieldname] for value in dep.equipment_set.all().values(fieldname)])
        else:
           for dep in self.department_set.all():
               equips.extend(dep.equipment_set.all())
        return equips

    def workers_count(self):
        return self.staff_set.filter(workers_count=True).count()

    def get_last_red(self):
        reds = self.risksevaluationdocument_set.order_by('-record_date')
        if reds:
            return reds[0]
        else:
            return None

    def get_changes(self):
        from accounts.models import Activity
        cc = ContentType.objects.get(app_label='customers', model='customercompany')
        staff = ContentType.objects.get(app_label='customers', model='staff')
        dep = ContentType.objects.get(app_label='customers', model='department')
        secduty = ContentType.objects.get(app_label='customers', model='companysecurityduty')
        equip = ContentType.objects.get(app_label='customers', model='equipment')

        acts_on_cc = Activity.objects.filter(in_revision=None,
                                             content_type=cc,
                                             object_id=self.id)

        staff_ids = [value['id'] for value in self.staff_set.values('id')]
        acts_on_staff = Activity.objects.filter(in_revision=None,
                                             content_type=staff,
                                             object_id__in=staff_ids)

        dep_ids = [value['id'] for value in self.department_set.values('id')]
        acts_on_deps = Activity.objects.filter(in_revision=None,
                                               content_type=dep,
                                               object_id__in=dep_ids)

        secduty_ids = [value['id'] for value in self.companysecurityduty_set.values('id')]
        acts_on_secdutys = Activity.objects.filter(in_revision=None,
                                               content_type=secduty,
                                               object_id__in=secduty_ids)

        equip_ids = self.equipments(fieldname='id')
        acts_on_equips = Activity.objects.filter(in_revision=None,
                                                 content_type=equip,
                                                 object_id__in=equip_ids)

        acts = list()
        if acts_on_cc:
            acts.extend(acts_on_cc)
        if acts_on_staff:
            acts.extend(acts_on_staff)
        if acts_on_deps:
            acts.extend(acts_on_deps)
        if acts_on_equips:
            acts.extend(acts_on_equips)
        return acts

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
    size = models.PositiveIntegerField(_('Department size mq.'))

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

    appoint_letter = models.FileField(_('Appoint Letter'),
                                      null=True,
                                      blank=True,
                                      upload_to='document_attaches')
    requirement_certificate = models.FileField(_('Requirement Certificate'),
                                               null=True,
                                               blank=True,
                                               upload_to='document_attaches')

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

class Equipment(models.Model):
    name = models.CharField(_('Name'), max_length=200)
    code = models.CharField(_('Code'), max_length=200)
    description = models.TextField(_('Description'), blank=True, null=True)
    department = models.ForeignKey(Department, verbose_name=_('Department'))
    operator = models.ForeignKey(Staff, null=True, blank=True, verbose_name=_('Operator'),
                                 related_name='equipment_operated')
    exposed_staff = models.ManyToManyField(Staff, verbose_name=_('Exposed staff'),
                                           null=True,
                                           blank=True,
                                           related_name='exposed_to'
                                           )
    compliance_requirement = models.CharField(_('Compliance Requirements'), max_length=255)
    record_by = models.ForeignKey('accounts.UserProfile',
                                  related_name='equipment_created',
                                  verbose_name=_('Recorded by'))
    lastupdate_by = models.ForeignKey('accounts.UserProfile',
                                    related_name='equipment_edited',
                                    verbose_name=_('Last update by'))
    record_date = models.DateTimeField(_('Recorded on'), auto_now_add=True)

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.code)

    class Meta:
        verbose_name = _('Equipment')
        verbose_name_plural = _('Equipment')

class DPI(models.Model):
    name = models.CharField(_('Name'), unique=True, max_length=200)
    description = models.CharField(_('Description'), max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Individual Protection Equipment')
        verbose_name_plural = _('Individual Protection Equipments')
