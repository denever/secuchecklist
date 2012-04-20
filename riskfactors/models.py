from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

# Create your models here.

class RiskFactor(models.Model):
    description = models.CharField(_('Description'), max_length=200, null=True, blank=True)
    question = models.TextField(_('Question'), null=True, blank=True)
    measure = models.TextField(_('Measure'), null=True, blank=True)
    suggestion_yes = models.TextField(_('Suggestion yes'), null=True, blank=True)
    suggestion_no = models.TextField(_('Suggestion No'), null=True, blank=True)
    notes = models.TextField(_('Notes'), null=True, blank=True)
    link = models.CharField(_('Link'), max_length=200, null=True, blank=True)
    filename = models.FileField(_('Filename'), null=True, blank=True, upload_to='riskfactor_attaches')
    parent = models.ForeignKey('self', null=True, blank=True,
                               verbose_name=_('parent'),
                               related_name='children')
    record_date = models.DateTimeField(_('Record date'), auto_now_add=True)

    code = models.CharField(_('Code'), max_length=200, null=True, blank=True, unique=True)
    parent_code = models.CharField(_('Parent code'), max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.description

    class Meta:
        ordering = ['code']
        verbose_name = _('Risk Factor')
        verbose_name_plural = _('Risk Factors')

import reversion

reversion.register(RiskFactor)
