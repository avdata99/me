# -*- coding: utf-8 -*-
"""
buscar correlaciones en cada provincia mayores a 'min_correl'
uso: xx.py min_correl(0.0/1.0) just_porc(1/0) compare_vars
compare_vars: una o mas variables que se van a comparar contra todas (o solo las _PORC)
ejemplo, relacionar conyuges contra todas las variables de porcentaje y listar las que tengan mas de 0.95
python 05-json_to_best_correl.py 0.95 1 P__01_02
"""
import sys
import json
from pkg import constantes

min_correl = float(sys.argv[1])
just_porc = True if sys.argv[2] == "1" else False
compare_vars = sys.argv[3:]

def get_high_regresion(cod_prov, min_correl=0.90, just_porc = True, compare_vars = None):
    """
    # analizar los datos de cada provincia todos los valores y guardar solo los que tienen mayor correlacion
    (min_corr = 0.85 minima correlacion (abs) para tener en cuenta el dato)
    just_porc: Solo variables que sean porcentuales de total (sufijo _PORC)
    """
    json_data = open('datajson/censo2010.%s.json' % str(cod_prov))
    data = json.load(json_data)
    json_data.close()

    num_fields = []
    for k, v in data[0].iteritems():
        if type(v) in [int, float]:
            if just_porc and k not in compare_vars:
                if k[-5:] != "_PORC":
                    continue
            num_fields.append(k)

    series = {}
    for r in data:
        for k, v in r.iteritems():
            #some fields are numeric but I dont care now
            if k in [u'Provincia', u'Depto', u'Fraccion', u'Fraccion_Full', u'radio_full', u'Depto_Full', u'Radio', u'Personas', u'Hogares', u'Viviendas']:
                continue
            if k in num_fields:
                if series.get(k, False) == False:
                    series[k] = []
                series[k].append(v)

    import numpy as np # importar numpy para manejo de matrices y otros calculos
    ret = []

    if compare_vars == None or compare_vars == []:
        compare_vars = series.keys()
    for k in compare_vars:
        for k2, v2 in series.iteritems():
            var1_name = k.split("__")[0] + "__ " + k.split("__")[1].split("_")[0]
            var2_name = k2.split("__")[0] + "__ " + k2.split("__")[1].split("_")[0]

            # no comparar variables del mismo grupo ya que necesariamente habra correlacion y hace ruido
            if var1_name == var2_name:
                continue

            # descartar algunos agrupadores
            if var1_name == "V__INCALCONS" or var2_name == "V__INCALCONS":
                continue

            if var1_name == "V__INCALSERV" or var2_name == "V__INCALSERV":
                continue

            if var1_name == "V__INMAT" or var2_name == "V__INMAT":
                continue


            if k != k2:
                f1 = constantes.getFlds(k)
                f2 = constantes.getFlds(k2)
                # revisar covarianza
                len_k_serie = len(series[k])
                len_k2_serie = len(series[k2])
                xy = np.vstack((series[k], series[k2]))
                cv = np.cov(xy)
                covar = u"%.3f" % (cv[1][0]) # covarianza
                # calcular coeficiente de correlacion
                cc = np.corrcoef(xy)
                ccv = u"%.3f" % (cc[1][0]) # valor del coeficiente de correlacion
                ccv_abs = u"%.3f" % (abs(cc[1][0])) # valor del coeficiente de correlacion
                if abs(cc[1][0]) > min_correl:
                    ret.append([k, k2, f1, f2, ccv, ccv_abs, covar, len_k_serie, len_k2_serie])

    return ret

# hacer un analisis de regresion de todas las variables en todas las provincias

print "Regresioning (?) ..."
vr = "ALL" if len(compare_vars) == 0 else str(compare_vars[0])
g = open("correl/censo2010.correlacion.%s.%s.%s.csv" % (vr, str(min_correl), str(just_porc)), "w")
g.write("id_prov;prov;var1;var2;svar1;svar2;value;value_abs;covar;len_serie1;len_serie2\n")

for k, v in constantes.Provincias.iteritems():
    print "Regresion for %s" % v
    ret = get_high_regresion(k, min_correl, just_porc, compare_vars)
    for r in ret:
        line = u"%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s\n" % (k.decode('utf-8'), v.decode('utf-8'), r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8])
        g.write(line.encode("utf-8"))

g.close()

