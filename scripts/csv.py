import pandas as pd

from classes.graph import Graph
from classes.node import Node


def getNodesData(graph: Graph):
    # Leer el archivo de Excel
    data_frame = pd.read_excel("data/nodeData.xlsx")

    # Iterar sobre cada fila
    for index, row in data_frame.iterrows():
        # Acceder a los valores de cada columna
        code = row['code']
        name = row['name']
        requireVisa = str(row['requireVisa']) == '1'
        node = Node(code, name, requireVisa)
        graph.addNode(node)


def getEdgesData(graph: Graph):
    # Leer el archivo de Excel
    data_frame = pd.read_excel("data/edgesData.xlsx")

    # Iterar sobre cada fila
    for index, row in data_frame.iterrows():
        # Acceder a los valores de cada columna
        orig = row['origin']
        dest = row['destination']
        cost = float(row['price'])
        graph.addEdge(orig, dest, cost)
