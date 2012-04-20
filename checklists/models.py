from django.db import models
from django.utils.translation import ugettext as _

# depends on django-simple-history
# from simple_history.models import HistoricalRecords

# Create your models here.
class CheckList(models.Model):
    company = models.ForeignKey('customers.CustomerCompany')

    history = HistoricalRecords()

    record_by = models.ForeignKey('accounts.UserProfile',
                                  related_name='checklists_created',
                                  verbose_name=_('Recorded by'))
    lastupdate_by = models.ForeignKey('accounts.UserProfile',
                                      related_name='checklists_edited',
                                      verbose_name=_('Last update by'))
    record_date = models.DateTimeField(_('Recorded on'), auto_now_add=True)

class RiskFactorEvaluation(models.Model):
    checklist = models.ForeignKey(CheckList)
    risk_factor = models.ForeignKey('riskfactors.RiskFactor')
    answer = models.BooleanField(_('Answer'))

    record_by = models.ForeignKey('accounts.UserProfile',
                                  related_name='evaluations_created',
                                  verbose_name=_('Recorded by'))
    lastupdate_by = models.ForeignKey('accounts.UserProfile',
                                      related_name='evaluations_edited',
                                      verbose_name=_('Last update by'))
    record_date = models.DateTimeField(_('Recorded on'), auto_now_add=True)
