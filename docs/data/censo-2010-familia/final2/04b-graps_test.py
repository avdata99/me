# -*- coding: utf-8 -*-
"""
Hacer un grafico de una o más variables
uso
python nnn.py grap_type prov
grap_type: boxplot |
prov: cod_prov | varios codigos separados por comas | 0 for all


"""

import json
import sys
from pkg import constantes

graph_type = sys.argv[1]

prov = sys.argv[2]
if prov == "0":
    provs = constantes.Provincias.keys()
else:
    provs = prov.split(",")

variables = sys.argv[3:]


data = {}
data_series = {}
for k in provs:
    json_data = open('datajson/censo2010.%s.json' % k)
    data[k] = json.load(json_data)
    json_data.close()

    # pasar a datos como series
    series = {}
    for r in data[k]: # iterar cada registro
        for k2 in variables: # leer solo las variables que voy a usar
            if series.get(k2, False) == False:
                series[k2] = []
            series[k2].append(r[k2])

    # agregar todas estas series a el diccionario general que tiene un registro por provincia
    if data_series.get(k, False) == False:
        data_series[k] = {}
    data_series[k] = series


import matplotlib.pyplot as plt # importar librería gráfica
# import numpy as np

ix = 1
iy = 1
gs = len(variables) * len(provs)
if gs > 3:
    iy = 2 + ( ((gs - 6) / 3 ) + 1)
    gs = 3

fig = plt.figure(figsize=(16, iy * 4)) # cada punto son 80 pixeles. 16 es todo el ancho de mi pantalla aprox.
fig.subplots_adjust(hspace=0.35)
fig.suptitle('Graph', fontsize=8, fontweight='bold')

for p in provs:
    for v in variables:
        ax = fig.add_subplot(iy, gs, ix)
        ix += 1

        tit = '[%s] %s en %s' % (v, constantes.getFlds(v), constantes.Provincias[p].decode("utf-8"))
        ax.set_title(tit, fontsize=8)
        """
        ax.set_xlabel(constantes.getFlds(k1), fontsize=8)
        ax.set_ylabel(constantes.getFlds(k2), fontsize=8)
        """
        if graph_type == "boxplot":
            plt.boxplot(data_series[p][v])
        if graph_type == "hist":
            plt.hist(data_series[p][v])

plt.show()
