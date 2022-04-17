import pandas as pd
import numpy as np
import networkx as nx

archivo = open('calles_de_medellin_con_acoso.csv', "r")
lineas = archivo.readlines()
elementos = []
for linea in lineas:
    elementos.append(linea.split(";"))


print("Ingrese su lugar de inicio.")
inicio=input()
print("Ingrese el lugar al que quiere llegar.")
objetivo=input()
df = pd.read_csv('calles_de_medellin_con_acoso.csv',sep=";")
mapa = nx.from_pandas_edgelist(df,source='origin',target='destination',edge_attr='length')
camino = nx.dijkstra_path(mapa, source=inicio, target=objetivo, weight=True)
print("El camino más corto para llegar a su destino es:")
print(camino)
