from django.core.management.base import BaseCommand, CommandError
from checklists.models import RiskFactor

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
                             codice=desc[8].strip('/'),
                             codice_padre=codice_padre.strip('/'))
            obj.save()
        for risk_factor in RiskFactor.objects.all():
            risk_factor.belongs_to = RiskFactor.objects.get(codice=risk_factor.codice_padre)
            risk_factor.save()
