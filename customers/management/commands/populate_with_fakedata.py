# encoding: utf-8

from django.core.management.base import BaseCommand, CommandError
from customers.models import CollaborationAgreement, Role, StandardTask

class Command(BaseCommand):
    """
    Populate db with fake data for CollaborationAgreeement, Role, StandardTask
    """
    help = 'Populate db with fake data for CollaborationAgreeement, Role, StandardTask'

    def handle(self, *args, **options):
        roles = [_('Datore di lavoro'),
                 _('Dirigente'),
                 _('Operaio'),
                 _('Segretaria'),
                 _('Ingegnere'),
                 ]

        for role in roles:
            obj = Role(name=role, description=role)
            obj.save()

        obj = CollaborationAgreement(name=_('Schiavitù'), description=_('Frustate'))
        obj.save()

        obj = StandardTask(name=_('Videoterminalista'), description=_('Videoterminalista'))
        obj.save()
