from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.
class Checklist(models.Model):
    company = models.ForeignKey('customers.CustomerCompany')

    title = models.CharField(_('Title'), max_length=255)
    
    record_by = models.ForeignKey('accounts.UserProfile',
                                  related_name='checklists_created',
                                  verbose_name=_('Recorded by'))
    lastupdate_by = models.ForeignKey('accounts.UserProfile',
                                      related_name='checklists_edited',
                                      verbose_name=_('Last update by'))
    record_date = models.DateTimeField(_('Recorded on'), auto_now_add=True)

class RiskFactorEvaluation(models.Model):
    checklist = models.ForeignKey(Checklist)
    risk_factor = models.ForeignKey('riskfactors.RiskFactor')
    answer = models.BooleanField(_('Answer'))

    record_by = models.ForeignKey('accounts.UserProfile',
                                  related_name='evaluations_created',
                                  verbose_name=_('Recorded by'))
    lastupdate_by = models.ForeignKey('accounts.UserProfile',
                                      related_name='evaluations_edited',
                                      verbose_name=_('Last update by'))
    record_date = models.DateTimeField(_('Recorded on'), auto_now_add=True)


import reversion

reversion.register(Checklist)
reversion.register(RiskFactorEvaluation)
