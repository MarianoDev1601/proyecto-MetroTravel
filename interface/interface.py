import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from classes.graph import Graph

from scripts.csv import *
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def originsList(graph: Graph):
    origins = []
    for node, neighbors in graph.graph.items():
        origins.append(node)
    return origins

def destinationsList(graph: Graph):
    destinations = []
    for node, neighbors in graph.graph.items():
        destinations.append(node)
    return destinations

def drawGraphNX(graph: Graph, shortestPath, shortestEdge):
    g = nx.Graph()
    # Agregar nodos y aristas al grafo
    for node, neighbors in graph.graph.items():
        for neighbor, cost in neighbors:
            g.add_edge(node, neighbor, weight=cost) # Add edge weight to graph

    # Crear un layout para el grafo
    pos = nx.spring_layout(g, seed=900)

    # Seleccion de color para los Grafos con visa 
    node_colors_visa = {'CCS':'blue','AUA':'red','BON':'red','CUR':'red','SXM':'red','SDQ':'red', 'SBH':'blue','POS':'blue','BGI':'blue','FDF':'blue','PTP':'blue'}

    # Diccionario para elegir el color del path tomado para el camino mas corto
    node_colors_shortestPath = {}

    # Diccionario para elegir el color de los edges tomados para el camino mas corto
    node_colors_shortestEdge = {}

    # Diccionario para agregarle le peso al camino usado
    edge_labels = {}

    #For loop para agregar los datos a cada diccionario
    for node in g.nodes():
        if node in shortestPath:
            node_colors_shortestPath[node] = "yellow"
        else:
            node_colors_shortestPath[node] = "gray"

        if shortestEdge and node == shortestEdge[0][0]:
            for node2 in g.nodes():
                if node2 == shortestEdge[0][1]:
                    node_colors_shortestEdge[(node,node2)] = 'red'
                    edge_labels[(node, node2)] = g[node][node2]['weight']
                else:
                    node_colors_shortestEdge[(node,node2)] = 'gray'
        elif shortestEdge and node == shortestEdge[0][1]:
            for node2 in g.nodes():
                if node2 == shortestEdge[0][0]:
                    node_colors_shortestEdge[(node,node2)] = 'red'
                    edge_labels[(node, node2)] = g[node][node2]['weight']
                else:
                    node_colors_shortestEdge[(node,node2)] = 'gray'
        elif shortestEdge and node == shortestEdge[1][0]:
            for node2 in g.nodes():
                if node2 == shortestEdge[1][1]:
                    node_colors_shortestEdge[(node,node2)] = 'red'
                    edge_labels[(node, node2)] = g[node][node2]['weight']
                else:
                    node_colors_shortestEdge[(node,node2)] = 'gray'
        elif shortestEdge and node == shortestEdge[1][1]:
            for node2 in g.nodes():
                if node2 == shortestEdge[1][0]:
                    node_colors_shortestEdge[(node,node2)] = 'red'
                    edge_labels[(node, node2)] = g[node][node2]['weight']
                else:
                    node_colors_shortestEdge[(node,node2)] = 'gray'
        else:
            node_colors_shortestEdge[node] = 'gray'

    #Colores para el grafo
    colors_shortestPath = [node_colors_shortestPath[node] for node in g.nodes()]
    colors_shortestEdge = [node_colors_shortestEdge.get(edge, 'gray') for edge in g.edges()]

    # Dibujar el grafo
    nx.draw(g, pos=pos, with_labels=True, node_size=600, node_color=colors_shortestPath, font_size=10, edge_color=colors_shortestEdge, width=1, alpha=0.7)

    # Dibujar las etiquetas de las aristas
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels, font_color='black')

    # Mostrar el gráfico
    plt.show()
    return

def printRoute(graph, origin, destination, visa, pathType):  
    if(origin.get() != "" and destination.get() != "" and visa.get() != "" and pathType.get() != ""):
        try:
            print("GAFOOOOOO", origin.get(), destination.get(), visa.get(), pathType.get())

            startNode = origin.get()
            end_node = destination.get()
            
            path = pathType.get()
            
            if visa.get() == "Si":
                hasVisa = True
            elif visa.get() == "No":
                hasVisa = False
                
            
            if path == "Ruta con menos paradas":
                shortest_distance, shortest_path, shortest_edge = graph.findShortestStopPath(
                    startNode, end_node, hasVisa)
                drawGraphNX(graph, shortest_path, shortest_edge)
                
            elif path == "Ruta más barata":
                shortest_distance, shortest_path, shortest_edge = graph.findShortestPath(
                    startNode, end_node, hasVisa)
                drawGraphNX(graph, shortest_path, shortest_edge)
            
        except:
            errorDialog()
    else:
        validateDialog()

def validateDialog():
    messagebox.showerror("Error", "Asegurese de rellenar todos los campos.")
    
def errorDialog():
    messagebox.showerror("Error", "Error al buscar la ruta.")

def start(graph: Graph):
    interface = tk.Tk()
    interface.title("MetroTravel")

    interface.configure(bg="orange")
    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 12), background="orange")
    style.configure("TButton", font=("Arial", 12))

    title = ttk.Label(interface, text="Bienvenido a MetroTravel", font=("Arial", 20), background="orange")
    title.grid(row=0, column=0, columnspan=5, pady=10)

    originsLabel = ttk.Label(interface, text="País de Origen:", style="TLabel")
    originsLabel.grid(row=1, column=0, padx=10, sticky="w")
    origins = originsList(graph)
    origin = ttk.Combobox(interface, values=origins)
    origin.grid(row=2, column=0, padx=10)

    destinationLabel = ttk.Label(interface, text="País de Destino:", style="TLabel")
    destinationLabel.grid(row=1, column=1, padx=10, sticky="w")
    destinations = destinationsList(graph)
    destination = ttk.Combobox(interface, values=destinations)
    destination.grid(row=2, column=1, padx=10)

    visaLabel = ttk.Label(interface, text="¿Cuenta con Visa?:", style="TLabel")
    visaLabel.grid(row=1, column=2, padx=10, sticky="w")
    visa = ttk.Combobox(interface, values=["Si", "No"])
    visa.grid(row=2, column=2, padx=10)

    pathLabel = ttk.Label(interface, text="Tipo de ruta:", style="TLabel")
    pathLabel.grid(row=1, column=3, padx=10, sticky="w")
    pathType = ttk.Combobox(interface, values=["Ruta más barata", "Ruta con menos paradas"])
    pathType.grid(row=2, column=3, padx=10)

    travel = ttk.Button(interface, text="Buscar...", command=lambda: printRoute(graph, origin, destination, visa, pathType), style="TButton")
    travel.grid(row=3, column=0, columnspan=5, pady=20)

    interface.mainloop()
    
    