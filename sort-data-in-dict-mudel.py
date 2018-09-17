from collections import Counter
import pandas as pd
from pprint import pprint

df = pd.read_csv('yv-data-4.csv', encoding='utf-8')


mark = df['MARK'].values.tolist()
mudel = df['MUDEL'].values.tolist()
valjalaskeaasta = df['VÄLJALASKEAASTA'].values.tolist()
koduva_yv_protsent = df['KORDUVA ÜV PROTSENT'].values.tolist()
soidukite_vanus = df['SOIDUKITE VANUS'].values.tolist()
soidukite_arv = df['SOIDUKITE ARV'].values.tolist()

carmakers = []

car_makers = ['MERCEDES-BENZ', 'BMW', 'FORD', 'HONDA', 'VOLKSWAGEN', 'VOLVO', 'SUZUKI', 'TOYOTA', 'OPEL', 'CHEVROLET',
              'AUDI', 'NISSAN', 'RENAULT', 'MITSUBISHI', 'FIAT', 'PEUGEOT', 'CITROEN', 'MAZDA', 'HYUNDAI', 'DODGE',
              'PORSCHE', 'CHRYSLER', 'KIA', 'LEXUS', 'CADILLACK', 'JEEP', 'SEAT', 'LAND ROVER', 'SKODA', 'SUBARU',
              'JAGUAR', 'SAAB', 'ALFA ROMEO', 'PONTIAC', 'LINCOLN', 'ISUZU', 'BUICK', 'DAEWOO', 'INFINITI', 'LANCIA',
              'DACIA', 'SMART', 'CADILLAC']

for carmaker in Counter(mark).most_common(100):
    carmakers.append(carmaker[0])

dict_of_cars = {}

for i in range(len(mark) - 1):
    if soidukite_arv[i] < 50:
        continue

    if mark[i] not in car_makers:
        continue

    #if koduva_yv_protsent[i] > float(5):
    #    continue

    if valjalaskeaasta[i] > int(2008):
        continue

    #if mark[i] not in dict_of_cars.keys():
    #    dict_of_cars[mark[i]] = {}

    # if mudel[i] not in dict_of_cars[mark[i]][mudel[i]].keys():
    #     dict_of_cars[mark[i]][mudel[i]] = {}

    dict_of_cars[mark[i] + ' ' + mudel[i] + ' ' + str(valjalaskeaasta[i])] = {
        'valjalaskeaasta': valjalaskeaasta[i],
        'koduva_yv_protsent': koduva_yv_protsent[i],
        'soidukite_arv': soidukite_arv[i]
    }

    # dict_of_cars[mark[i]]['valjalaskeaasta'] = valjalaskeaasta[i]
    # dict_of_cars[mark[i]]['koduva_yv_protsent'] = koduva_yv_protsent[i]
    # dict_of_cars[mark[i]]['soidukite_arv'] = soidukite_arv[i]


pprint(sorted(dict_of_cars.items(), key=lambda x: x[1]['koduva_yv_protsent']))


# I want to connenct car models with lines so I can see, which is consistently the best.
# I have to recognize which models are acually the same.

#def does_my_dataset_already_contain_this_model(car_mark, car_model, car)