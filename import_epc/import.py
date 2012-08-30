import sqlite3
from customers.models import AtecoSector, Certification, CPISettlement, HealthSurveillance

conn = sqlite3.connect('data.db')
src_cur = conn.cursor()

src_cur.execute('select descrizione from SettoriATECO')
for desc in src_cur:
    obj = AtecoSector(name=desc[0], description=desc[0])
    obj.save()

src_cur.execute('select descrizione from Certificazioni')
for desc in src_cur:
    print desc[0]
    obj = Certification(short_name=desc[0], name=desc[0], description=desc[0])
    obj.save()

src_cur.execute('select descrizione from InsediamentiCPI')
for desc in src_cur:
    obj = CPISettlement(name=desc[0], description=desc[0])
    obj.save()

src_cur.execute('select descrizione from SorvSani')
for desc in src_cur:
    print desc[0]
    obj = HealthSurveillance(name=desc[0], description=desc[0])
    obj.save()
