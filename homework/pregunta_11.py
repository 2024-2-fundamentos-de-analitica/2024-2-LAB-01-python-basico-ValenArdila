"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    
    import csv
    col_2 = []
    col_4 = []
    with open(r"files\input\data.csv") as file:
        csv_reader = csv.reader(file, delimiter='\t')
        
        letras = ('a', 'b', 'c', 'd', 'e', 'f', 'g') 
        dicc = {}
        for letra in letras:
            dicc[letra] = 0
            
        for row in csv_reader:
            col_2.append(row[1])
            col_4.append(row[3])
    
        for num, letras in zip(col_2, col_4):
            for letra in letras.split(','):
                dicc[letra] += int(num)
    return dicc