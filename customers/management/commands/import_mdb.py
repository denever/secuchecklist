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

        src_cur.execute('select descrizione from SettoriATECO')
        for desc in src_cur:
            print desc[0]
            # obj = AtecoSector(name=desc[0], description=desc[0])
            # obj.save()
            
        src_cur.execute('select descrizione from Certificazioni')
        for desc in src_cur:
            print desc[0]
            # obj = Certification(short_name=desc[0], name=desc[0], description=desc[0])
            # obj.save()

        src_cur.execute('select descrizione from InsediamentiCPI')
        for desc in src_cur:
            print desc[0]
            # obj = CPISettlement(name=desc[0], description=desc[0])
            # obj.save()

        src_cur.execute('select descrizione from SorvSani')
        for desc in src_cur:
            print desc[0]
            # obj = HealthSurveillance(name=desc[0], description=desc[0])
            # obj.save()
