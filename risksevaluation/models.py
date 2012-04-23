from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.
class RisksEvaluationDocument(models.Model):
    company = models.ForeignKey('customers.CustomerCompany')
    revision = models.AutoField(_('Revision'), primary_key=True)
    revision_description = models.TextField(_('Revision description'))
    record_date = models.DateTimeField(_('Revision Date'), auto_now_add=True)

    record_by = models.ForeignKey('accounts.UserProfile',
                                  related_name='risksevaluationdocument_created',
                                  verbose_name=_('Recorded by'))
    lastupdate_by = models.ForeignKey('accounts.UserProfile',
                                      related_name='risksevaluationdocument_edited',
                                      verbose_name=_('Last update by'))

    rls_check = BooleanField(_('RLS check'))
    doctor_check = BooleanField(_('Doctor check'))
    companyowner_check = BooleanField(_('Doctor check'))

    def __unicode__(self):
        return '(%s %s)' % (self.revision, self.record_date)

    class Meta:
        ordering = ['record_date']
        verbose_name = _('Risks Evaluation Document')
        verbose_name_plural = _('Risks Evaluation Documents')
        unique_together = ('company','revision', 'record_date')

class RiskFactorEvaluation(models.Model):
    document = models.ForeignKey(RisksEvaluationDocument)
    risk_factor = models.ForeignKey('riskfactors.RiskFactor')
    answer = models.BooleanField(_('Answer'))

    record_by = models.ForeignKey('accounts.UserProfile',
                                  related_name='factorevaluations_created',
                                  verbose_name=_('Recorded by'))
    lastupdate_by = models.ForeignKey('accounts.UserProfile',
                                      related_name='factorevaluations_edited',
                                      verbose_name=_('Last update by'))
    record_date = models.DateTimeField(_('Recorded on'), auto_now_add=True)

    class Meta:
        ordering = ['record_date']
        verbose_name = _('Risk Factor Evaluation')
        verbose_name_plural = _('Risk Factor Evaluations')

import reversion

reversion.register(RisksEvaluationDocument)
reversion.register(RiskFactorEvaluation)
