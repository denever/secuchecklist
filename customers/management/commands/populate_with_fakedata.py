# encoding: utf-8

from django.core.management.base import BaseCommand, CommandError
from customers.models import CollaborationAgreement, Role, StandardTask

class Command(BaseCommand):
    """
    Populate db with fake data for CollaborationAgreeement, Role, StandardTask
    """
    help = 'Populate db with fake data for CollaborationAgreeement, Role, StandardTask'

    def handle(self, *args, **options):
        roles = ['Datore di lavoro',
                 'Dirigente',
                 'Operaio',
                 'Segretaria',
                 'Ingegnere',
                 ]

        for role in roles:
            obj = Role(name=role, description=role)
            obj.save()

        obj = CollaborationAgreement(name='Schiavitù', description='Frustate')
        obj.save()

        obj = StandardTask(name='Videoterminalista', description='Videoterminalista')
        obj.save()
