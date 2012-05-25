from django.core.management.base import BaseCommand, CommandError
from django.utils.translation import ugettext as _

from customers.models import Nationality, SecurityDuty

# importing User for UserProfile
from django.contrib.auth.models import User
from accounts.models import UserProfile


class Command(BaseCommand):
    """
    Populate db with utility data for Nationality, SecurityDuty
    """
    help = 'Populate db with utility data for Nationality, SecurityDuty'

    def handle(self, *args, **options):
	duties = [_('Datore di lavoro'),
		  _('Datore di lavoro con funzioni RSPP'),
		  _('RSPP'),
		  _('Dirigente'),
		  _('Preposto'),
		  _('RLS'),
		  _('ASPP'),
		  _('Medico competente'),
		  _('Addetto al primosoccorso'),
		  _('Adetto alle emergenze/antincendio')
		  ]

	for duty in duties:
	    obj = SecurityDuty(name=duty, description=duty)
	    obj.save()

	obj = Nationality(nationality=_('Italiana'))
	obj.save()

	u = User.objects.get(id=1)
	up = UserProfile(user=u)
	up.save()
