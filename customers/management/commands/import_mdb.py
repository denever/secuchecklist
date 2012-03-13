from django.core.management.base import BaseCommand, CommandError
from customers.models import AtecoSector, Certification, CPISettlement, HealthSurveillance

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
            obj = AtecoSector(name=desc[2], description=desc[2])
            obj.save()

        src_cur.execute('select * from Certificazioni')
        for desc in src_cur:
            obj = Certification(short_name=desc[1], name=desc[1], description=desc[1])
            obj.save()

        src_cur.execute('select * from InsediamentiCPI')
        for desc in src_cur:
            obj = CPISettlement(name=desc[1], description=desc[1])
            obj.save()

        src_cur.execute('select * from SorvSani')
        for desc in src_cur:
            obj = HealthSurveillance(name=desc[1], description=desc[1])
            obj.save()

        src_cur.execute('select codice, comune, provincia, cap from Comuni')
        for desc in src_cur:
            obj = TownShip(codice=desc[0], comune=desc[1], provincia=desc[2], cap=desc[3])
            obj.save()
