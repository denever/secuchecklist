from django.core.management.base import BaseCommand, CommandError
from riskfactors.models import RiskFactor

# before using this file
# apt-get install unixodbc libmdbodbc
# check the driver name in /etc/odbcinst.ini
import pyodbc
import os.path

QUERY_IMPORT="""
SELECT descrizione,
 domanda,
 misura,
 suggerimentosi,
 suggerimentono,
 note,
 link,
 nomefile,
 codice,
 pathid,
 pathlevel
FROM FattoriRischio
"""

class Command(BaseCommand):
    args = '<filename.mdb>'
    help = 'Import data from mdb files'

    def handle(self, *args, **options):
        DBfile = os.path.abspath(args[0])
        connect_str = 'DRIVER={MDBTools};DBQ=%s' % DBfile
        conn = pyodbc.connect(connect_str)
        src_cur = conn.cursor()

        src_cur.execute(QUERY_IMPORT)
        for desc in src_cur:
            codice_padre = str(desc[9]).split('/')[int(desc[10])]
            obj = RiskFactor(description=desc[0],
                             question=desc[1],
                             measure=desc[2],
                             suggestion_yes=desc[3],
                             suggestion_no=desc[4],
                             notes=desc[5],
                             link=desc[6],
                             filename=desc[7],
                             code=desc[8].strip('/'),
                             parent_code=codice_padre.strip('/'))
            obj.save()

        for risk_factor in RiskFactor.objects.all():
            if risk_factor.parent_code != '':
                risk_factor.parent = RiskFactor.objects.get(code=risk_factor.parent_code)
                print '_'*10
                print 'Child:', risk_factor
                print 'Child code:', risk_factor.code
                print 'Parent code:', risk_factor.parent_code
                print 'Parent:', risk_factor.parent
                print '#'*10
            else:
                print 'No father for', risk_factor
                risk_factor.parent = None
            risk_factor.save()
