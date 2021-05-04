# -*- coding: utf-8 -*-
"""
Sumar algunas variables de cada provincia y presentarlas en una tabla única
usage xxx.py save_as_sufix var1 var2 ... varN

var1 / var2: Codigo de las variables a comparar. Ej H__05_01, P__10_02
save_as_sufix: Sufijo para el nombre de archivo final
"""

import json
import sys
from pkg import constantes

def cumulate_vars(cod_prov, variables):
    json_data = open('datajson/censo2010.%s.json' % str(cod_prov))
    data = json.load(json_data)
    json_data.close()

    series = {}
    totales = {}
    for r in data:
        for k, v in r.iteritems():
            if k in variables:
                if series.get(k, False) == False:
                    series[k] = []
                    totales[k] = 0
                series[k].append(v)
                totales[k] = totales[k] + v

    return totales


# variables a comparar contra todas las otras
save_as = "acumulado/censo2010.acumulado.%s.csv" % sys.argv[1]
variables = sys.argv[2:]

print "Acumulando ..."
g = open(save_as, "w")
g.write("Id_Prov;Provincia")

for v in variables:
    g.write(";%s" % constantes.getFlds(v).encode("utf-8")  )

g.write("\n")

for k, v in constantes.Provincias.iteritems():
    g.write("%s;%s" % (k, v))
    print "Compare for %s" % v
    totales = cumulate_vars(k, variables)
    # for t, val in totales.iteritems():
    #    g.write(";%s" % str(val))
    for t in variables:
        g.write(";%s" % str(totales[t]))

    g.write("\n")

g.close()
