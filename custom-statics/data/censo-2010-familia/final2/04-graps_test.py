# -*- coding: utf-8 -*-
import json
from pkg import constantes

data = {}
data_series = {}
for k, v in constantes.Provincias.iteritems():
    json_data = open('datajson/censo2010.%s.json' % k)
    data[k] = json.load(json_data)
    json_data.close()

    # pasar a datos como series
    series = {}
    for r in data[k]:
        for k2, v2 in r.iteritems():
            if series.get(k2, False) == False:
                series[k2] = []
            series[k2].append(v2)

    if data_series.get(k, False) == False:
        data_series[k] = {}
    data_series[k] = series


import matplotlib.pyplot as plt # importar librería gráfica
import numpy as np

#variables a comparar

# si hay pareja, hay baño!!, muy bueno
graps = [["P10_02", "H01_01", ["14"]], ["P10_02", "H01_02", ["14"]]]
# hay conjuge = P10_02 # hay baño H01_01
# ver otras provincias

# si hay parejas, no hay NBI
graps = [["P10_02", "H05_01", ["94"]], ["P10_02", "H05_02", ["94"]]]


# parejas vs asiste, asistio, nunca asistio
graps = [["P10_02", "P08_01", ["14"]],["P10_02", "P08_02", ["14"]], ["P10_02", "P08_03", ["14"]]]

# P10_06 padres o suegros del jefe
graps = [["P10_06", "H05_01", ["14"]],["P10_06", "H05_02", ["14"]]]

# V08_0N tipo de vivienda -- CORDOBA
graps = [["P10_02", "V08_01", ["14"]],["P10_02", "V08_02", ["14"]],["P10_02", "V08_03", ["14"]]
        ,["P10_02", "V08_04", ["14"]],["P10_02", "V08_05", ["14"]],["P10_02", "V08_06", ["14"]]]
# claramente si hay pareja, hay casa
# estudia que pasa con los deptos

# con conyuges en CABA
graps = [["P10_02", "V08_01", ["2"]],["P10_02", "V08_02", ["2"]],["P10_02", "V08_03", ["2"]]
        ,["P10_02", "V08_04", ["2"]],["P10_02", "V08_05", ["2"]],["P10_02", "V08_06", ["2"]]]


# con conyuges en CABA
graps = [["P10_02", "V08_01", ["94"]],["P10_02", "V08_02", ["94"]],["P10_02", "V08_03", ["94"]]
        ,["P10_02", "V08_04", ["94"]],["P10_02", "V08_05", ["94"]],["P10_02", "V08_06", ["94"]]]


# no hay relacion entre los hijos y el NBI
graps = [["P10_03", "H05_01", ["14"]],["P10_03", "H05_02", ["14"]]
        ,["P10_03", "H05_01", ["2"]],["P10_03", "H05_02", ["2"]]]

graps = [["V06_01", "H05_01", ["78"]],["V06_01", "H05_02", ["78"]]
        ,["V06_01", "H05_01", ["2"]],["V06_01", "H05_02", ["2"]]]

graps = [["H__ALGUNBI_01", "P__10_02", ["78"]],["H__ALGUNBI_01", "P__10_02", ["10"]]
        ,["H__ALGUNBI_01_PORC", "P__10_02_PORC", ["78"]],["H__ALGUNBI_01_PORC", "P__10_02_PORC", ["10"]]]


graps = [["H__ALGUNBI_01_PORC", "P__01_02_PORC", []]]
graps = [["P__01_02_PORC", "H__ALGUNBI_01_PORC", ["14", "2", "6", "50"]]]
graps = [["P__01_03_PORC", "H__ALGUNBI_01_PORC", ["14", "2", "6", "50"]]]

graps = [["P__01_02_PORC", "V__01_01", ["14", "2", "6", "50"]]]

graps = [["V__URP_03_PORC", "H__09_01_PORC", []]]
graps = [["H__19A_01_PORC", "H__19C_01_PORC", []]]
graps = [["H__19B_01_PORC", "V__INCALCONS_01_PORC", []]]

# sin telefono de línea vs computadora
graps = [["H__19D_02_PORC", "H__19B_02_PORC", []]]
graps = [["P__01_01_PORC", "P__01_02_PORC", []]]
graps = [["P__01_03_PORC", "P__01_02_PORC", []]]
graps = [["P__01_01", "P__01_02", []]]
graps = [["P__01_03", "P__01_02", []]]
graps = [["H__05_01_PORC", "V__INCALCONS_01_PORC", []]]
graps = [["P__01_02_PORC", "V__INCALCONS_01_PORC", []]]


graps = [["P__01_02_PORC", "P__08_01_PORC", []]]
graps = [["P__01_03_PORC", "P__08_01_PORC", []]]

ix = 1
iy = 1
fig = plt.figure(figsize=(16, 32))
# fig = plt.figure()
fig.subplots_adjust(hspace=0.65)
for g in graps:
    k1=g[0]
    k2=g[1]
    if g[2] == []:
        g[2] = constantes.Provincias.keys()
    gs = len(graps) * len(g[2])
    if gs > 3:
        iy = 2 + ( ((gs - 6) / 3 ) + 1)
        gs = 3


    for k in g[2]:
        prov = constantes.Provincias[k]
        fig.suptitle('Dispersion', fontsize=8, fontweight='bold')
        ax = fig.add_subplot(iy, gs, ix)
        ix += 1
        xy = np.vstack((data_series[k][k1],data_series[k][k2]))
        cv = np.cov(xy)
        covar = "%.3f" % (cv[1][0]) # covarianza
        # calcular coeficiente de correlacion
        cc = np.corrcoef(xy)
        ccv = "%.3f" % (cc[1][0]) # valor del coeficiente de correlacion
        ccv_abs = "%.3f" % (abs(cc[1][0])) # valor del coeficiente de correlacion

        ax.set_title('%s Correl: %s' % (prov.decode("utf-8"), ccv))

        ax.set_xlabel(constantes.getFlds(k1), fontsize=8)
        ax.set_ylabel(constantes.getFlds(k2), fontsize=8)
        plt.scatter(data_series[k][k1], data_series[k][k2])

plt.show()
