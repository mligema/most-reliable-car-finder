

def korduva_yv_protsent(kokku_yv, korras_yv):
    return 100 - (korras_yv * 100) / kokku_yv

def korduva_yv_protsent_2(soidukite_arv, kordus):
    return (kordus * 100)/soidukite_arv

def korduva_yv_protsent_3(yv_käis, kordus):
    return (kordus * 100)/yv_käis

def korduva_yv_protsent_4(korras_yv, korduv_yv):
    return round((korduv_yv * 100)/(korras_yv + korduv_yv), 2)

print(korduva_yv_protsent(803, 660))

# avensis
print(korduva_yv_protsent(771, 674))
print(korduva_yv_protsent_2(663, 74))
print(korduva_yv_protsent_3(771, 74))
print(korduva_yv_protsent_4(674, 74))