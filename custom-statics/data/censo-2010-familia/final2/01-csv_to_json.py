# -*- coding: utf-8 -*-
"""
Leer el archivo de origen con los 50.000 radios en CSV y pasarlo a archivos JSON (uno por provincia)
Cada archivo guarda cada dato con su valor original y el porcentaje. Por ejemplo si de 200 personas
110 son mujeres y 90 hombres tambien se guardan el 55 y el 45%. Esto permite mejor deteccion de correlaciones.
Esto se debe a que la cantidad de viviendas, hogares y personas difiere mucho para cada medicion.
"""

import csv
import json
from pkg import constantes

def csv_to_json(path_file):

    """
    FULL DATA IN A SINGLE FILE
    data out = json.dumps( [ row for row in reader ] )
    g = open("censo2010.json", "w")
    g.write(out)
    """
    print "READING ..."

    for pr, pr_name in constantes.Provincias.iteritems():
        f = open(path_file, "r")
        reader = csv.DictReader(f, delimiter="\t")

        print "CREATING %s" % pr_name
        data = []
        for row in reader:
            if int(pr) != int(row["Provincia"]):
                continue

            new_row = {}
            for k,v in row.iteritems():
                try: # quiero los campos numericos como numeros para poder procesar despues
                    new_row[k] = int(v)
                except:
                    new_row[k] = v
                else:
                    if k[:3] == "V__":
                        nr = "%s_PORC" % k
                        if int(row["Viviendas"]) > 0:
                            new_row[nr] = round(100 * float(v) / float(row["Viviendas"]),3)
                        else:
                            new_row[nr] = 0

                    if k[:3] == "H__":
                        nr = "%s_PORC" % k
                        if int(row["Hogares"]) > 0:
                            new_row[nr] = round(100 * float(v) / float(row["Hogares"]),3)
                        else:
                            new_row[nr] = 0

                    if k[:3] == "P__":
                        nr = "%s_PORC" % k
                        if int(row["Personas"]) > 0:
                            new_row[nr] = round(100 * float(v) / float(row["Personas"]),3)
                        else:
                            new_row[nr] = 0

            data.append(new_row)

        print "SAVING %s (%s)" % (pr_name, len(data))
        g = open("datajson/censo2010.%s.json" % pr , "w")
        g.write(json.dumps(data))
        g.close()


# leer el archivo CSV con datos del censo por provincia y pasarlos a JSON
csv_to_json("ALL-RESULTS.csv")