from django.core.management.base import BaseCommand, CommandError
from customers.models import TownShip, Province

import sqlite3
import os.path

class Command(BaseCommand):
    args = '<trovacap.sql>'
    help = 'Import data from cap liberati FSFEurope'

    def handle(self, *args, **options):
        conn = sqlite3.connect('/tmp/trovacap.sqlite')
        trovacap_sql = open(args[0]).read()
        try:
            conn.executescript(trovacap_sql)
        except Exception, e:
            print e

        src_cur = conn.execute('select comu_cap, prov_cap, capi_cap from tab_cap group by comu_cap, prov_cap, capi_cap;')
        for desc in src_cur:
            obj = TownShip(name=desc[0], province=desc[1], zipcode=desc[2])
            obj.save()

        src_cur = conn.execute('select prov_cap from tab_cap group by prov_cap;')
        for desc in src_cur:
            obj = Province(province=desc[0])
            obj.save()
