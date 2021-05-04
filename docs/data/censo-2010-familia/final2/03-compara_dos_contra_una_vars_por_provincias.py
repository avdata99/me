# -*- coding: utf-8 -*-
"""
Comparar dos variables contra una en cada provincia y lista la correlacion
usage xxx.py var1 var2 save_as_sufix var_vs

var1 / var2: Codigo de las variables a comparar. Ej H__05_01, P__10_02
save_as_sufix: Sufijo para el nombre de archivo final
var_vs: variable contra la que las otras dos se comparan
"""

import json
import sys
import numpy as np # importar numpy para manejo de matrices y otros calculos
from pkg import constantes

# variables a comparar contra todas las otras
comparar = [sys.argv[1], sys.argv[2]]
var_vs = sys.argv[4]

def load_series(cod_prov):
    json_data = open('datajson/censo2010.%s.json' % str(cod_prov))
    data = json.load(json_data)
    json_data.close()

    num_fields = []
    for k, v in data[0].iteritems():
        if type(v) in [int, float]:
            num_fields.append(k)

    series = {}
    for r in data:
        for k, v in r.iteritems():
            #some fields are numeric but I dont care now
            if k in [u'Provincia', u'Fraccion', u'Fraccion_Full', u'Depto', u'radio_full', u'Depto_Full', u'Radio']:
                continue
            if k in num_fields:
                if series.get(k, False) == False:
                    series[k] = []
                series[k].append(v)

    return series


def compare_vars(cod_prov):
    k = var_vs
    print "Leyendo series de datos para %s" % constantes.Provincias[cod_prov]
    series = load_series(cod_prov)

    res_thin_line={}
    vals = {}
    for k2 in comparar:
        xy = np.vstack((series[k],series[k2]))
        cv = np.cov(xy)
        covar = "%.4f" % (cv[1][0]) # covarianza
        # calcular coeficiente de correlacion
        cc = np.corrcoef(xy)
        ccv = "%.4f" % (cc[1][0]) # valor del coeficiente de correlacion
        res_thin_line[k2] = [k, covar, ccv]
        vals[k2] = cc[1][0]

    return [res_thin_line[comparar[0]][0], res_thin_line[comparar[0]][2], res_thin_line[comparar[1]][2]]



print "Comparando ..."
g = open("compare/censo2010.compare.%s.csv" % sys.argv[3], "w")
g.write("Id_Prov;Provincia;variable;Correlacion %s;Correlacion %s\n" % (comparar[0], comparar[1]))

for k, v in constantes.Provincias.iteritems():
    print "Compare for %s" % v
    res = compare_vars(k)
    g.write("%s;%s;%s;%s;%s\n" % (k, v, res[0], res[1], res[2]))


g.close()
