from django.core.management.base import BaseCommand, CommandError
from customers.models import AtecoSector, Certification, CPISettlement
from customers.models import HealthSurveillance, TownShip, Province, DPI

# before using this file
# apt-get install unixodbc libmdbodbc
# check the driver name in /etc/odbcinst.ini
import pyodbc
import os.path

class Command(BaseCommand):
    args = '<filename.mdb>'
    help = 'Import data from mdb files'

    def handle(self, *args, **options):
        DBfile = os.path.abspath(args[0])
        connect_str = 'DRIVER={MDBTools};DBQ=%s' % DBfile
        conn = pyodbc.connect(connect_str)
        src_cur = conn.cursor()

        src_cur.execute('select * from SettoriATECO')
        for desc in src_cur:
            obj = AtecoSector(code=desc[1], name=desc[2], description=desc[2])
            obj.save()

        src_cur.execute('select * from Certificazioni')
        for desc in src_cur:
            obj = Certification(short_name=desc[1], name=desc[1], description=desc[1])
            obj.save()

        src_cur.execute('select * from InsediamentiCPI')
        for desc in src_cur:
            obj = CPISettlement(name=desc[1][:255], description=desc[1])
            obj.save()

        src_cur.execute('select * from SorvSani')
        for desc in src_cur:
            obj = HealthSurveillance(name=desc[1], description=desc[1])
            obj.save()

        src_cur.execute('select * from DPI')
        for desc in src_cur:
            obj = DPI(name=desc[1], description=desc[1])
            obj.save()

        # src_cur.execute('select codice, comune, provincia, cap from Comuni')
        # for desc in src_cur:
        #     if desc[3]:
        #         obj = TownShip(code=desc[0], name=desc[1], province=desc[2], zipcode=desc[3])
        #         obj.save()
        #     else:
        #         print 'Discarded:', desc

        # values = TownShip.objects.values('province').distinct()
        # for value in values:
        #     obj = Province(province=value['province'])
        #     obj.save()
