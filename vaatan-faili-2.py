from pprint import pprint
import pandas as pd
from collections import Counter

df = pd.read_csv('yv-data-4.csv', encoding='utf-8')

print(df.head(5))

mark = df['MARK'].values.tolist()
mudel = df['MUDEL'].values.tolist()
valjalaskeaasta = df['VÄLJALASKEAASTA'].values.tolist()
koduva_yv_protsent = df['KORDUVA ÜV PROTSENT'].values.tolist()
soidukite_vanus = df['SOIDUKITE VANUS'].values.tolist()
soidukite_arv = df['SOIDUKITE ARV'].values.tolist()

mark_mudel_aasta = []
koduva_yv_protsent_ = []
soidukite_vanus_ = []

car_makers = ['MERCEDES-BENZ', 'BMW', 'FORD', 'HONDA', 'VOLKSWAGEN', 'VOLVO', 'SUZUKI', 'TOYOTA', 'OPEL', 'CHEVROLET',
              'AUDI', 'NISSAN', 'RENAULT', 'MITSUBISHI', 'FIAT', 'PEUGEOT', 'CITROEN', 'MAZDA', 'HYUNDAI', 'DODGE',
              'PORSCHE', 'CHRYSLER', 'KIA', 'LEXUS', 'CADILLACK', 'JEEP', 'SEAT', 'LAND ROVER', 'SKODA', 'SUBARU',
              'JAGUAR', 'SAAB', 'ALFA ROMEO', 'PONTIAC', 'LINCOLN', 'ISUZU', 'BUICK', 'DAEWOO', 'INFINITI', 'LANCIA',
              'DACIA', 'SMART']

for i in range(len(mark) - 1):
    if soidukite_arv[i] < 30:
        continue

    if mark[i] not in car_makers:
        continue

    if koduva_yv_protsent[i] > float(5):
        continue

    if valjalaskeaasta[i] > int(2009):
        continue

    mark_mudel_aasta.append(str(mark[i] + ' ' + mudel[i] + ' ' + str(valjalaskeaasta[i]) + ' ' + str(soidukite_arv[i])))
    koduva_yv_protsent_.append(float(koduva_yv_protsent[i]))
    soidukite_vanus_.append(float(soidukite_vanus[i]))

print(len(mark_mudel_aasta))

from matplotlib import pyplot as plt

fig, ax = plt.subplots()
ax.scatter(koduva_yv_protsent_, soidukite_vanus_, s=1)

for i, txt in enumerate(mark_mudel_aasta):
    ax.annotate(txt, (koduva_yv_protsent_[i], soidukite_vanus_[i]), size=5, rotation=35)


plt.show()
