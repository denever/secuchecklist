from django.core.management.base import BaseCommand, CommandError
from riskfactors.models import RiskFactor


class Command(BaseCommand):
    args = '<filename.mdb>'
    help = 'Import data from mdb files'

    def print_riskfactor(self, rf, level=0):
        print '-'*level, rf
        for subrf in rf.children.all():
            self.print_riskfactor(subrf, level + 2)

    def handle(self, *args, **options):
        if len(args) > 0:
            rf = RiskFactor.objects.get(id=int(args[0]))
            self.print_riskfactor(rf)
        else:
            for rf in RiskFactor.objects.filter(parent__exact=None):
                self.print_riskfactor(rf)
