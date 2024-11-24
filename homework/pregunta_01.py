"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    import csv
    suma= 0

    with open(r"files\input\data.csv") as file:
        csv_reader = csv.reader(file, delimiter='\t')

        for row in csv_reader:
            suma+=int(row[1])
    return suma

            