from django.core.management.base import BaseCommand, CommandError

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
        duties = ['Datore di lavoro', 'RSPP',
                  'Dirigente',
                  'Preposto',
                  'RLS',
                  'ASPP',
                  'Medico competente',
                  'Addetto al primosoccorso',
                  'Adetto alle emergenze/antincendio'
                  ]

        for duty in duties:
            obj = SecurityDuty(name=duty, description=duty)
            obj.save()

        obj = Nationality(nationality='Italiana')
        obj.save()

        u = User.objects.get(id=1)
        up = UserProfile(user=u)
        up.save()
