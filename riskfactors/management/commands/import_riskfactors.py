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

        root_rf = RiskFactor(description='Fattori di Rischio', parent=None)
        root_rf.save()

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

        for risk_factor in RiskFactor.objects.exclude(id__exact=root_rf.id):
            if risk_factor.parent_code != '' and risk_factor.parent_code is not None:
                risk_factor.parent = RiskFactor.objects.get(code=risk_factor.parent_code)
            elif risk_factor != root_rf:
                risk_factor.parent = root_rf
            risk_factor.save()
