import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from classes.graph import Graph

from scripts.csv import *
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


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


def drawGraphNX(graph: Graph, shortestPath: list):
    g = nx.Graph()
    # Agregar nodos y aristas al grafo
    for node, neighbors in graph.graph.items():
        for neighbor, cost in neighbors:
            g.add_edge(node, neighbor, weight=cost)  # Add edge weight to graph

    # Crear un layout para el grafo
    posNX = nx.spring_layout(g, seed=900)

    # Seleccion de color para los Grafos con visa
    node_colors_visa = {'CCS': 'blue', 'AUA': 'red', 'BON': 'red', 'CUR': 'red', 'SXM': 'red',
                        'SDQ': 'red', 'SBH': 'blue', 'POS': 'blue', 'BGI': 'blue', 'FDF': 'blue', 'PTP': 'blue'}

    # Diccionario para elegir el color del path tomado para el camino mas corto
    node_colors_shortestPath = {}

    # Diccionario para elegir el color de los edges tomados para el camino mas corto
    node_colors_shortestEdge = {}

    # Diccionario para agregarle le peso al camino usado
    edge_labels = {}

    # For loop para agregar los datos a cada diccionario
    for node in g.nodes():
        origNode = ''
        destNode = ''
        if node in shortestPath:
            # Verificamos si tiene visa para pintarlo de un color u otro
            if (graph.nodes[node].visaRequired):
                node_colors_shortestPath[node] = "blue"
            else:
                node_colors_shortestPath[node] = "yellow"
            # Obtenemos la posición del nodo actual en la lista del camino
            pos = shortestPath.index(node)
            # Se verifica si el nodo que se está revisando es el último para poder setear correctamente el nodo origen y destino
            if (pos == len(shortestPath) - 1):
                origNode = shortestPath[pos - 1]
                destNode = shortestPath[pos]
            else:
                origNode = shortestPath[pos]
                destNode = shortestPath[pos + 1]
        # En caso de que no se encuentre en el camino a seguir, el nodo y su camino se pintan de gris y se sigue continua con el siguiente nodeo del for
        else:
            node_colors_shortestPath[node] = "gray"
            node_colors_shortestEdge[node] = 'gray'
            continue
        # En caso de que node se encuentre en el camino más corto, se pinta de rojo su arista y se coloca su peso para ser visualizado
        node_colors_shortestEdge[(origNode, destNode)] = 'red'
        edge_labels[(origNode, destNode)] = str(
            g[origNode][destNode]['weight'])

    # Colores para el grafo
    colors_shortestPath = [node_colors_shortestPath[node]
                           for node in g.nodes()]
    colors_shortestEdge = [node_colors_shortestEdge.get(
        edge, 'gray') for edge in g.edges()]

    # Dibujar el grafo
    nx.draw(g, pos=posNX, with_labels=True, node_size=600, node_color=colors_shortestPath,
            font_size=10, edge_color=colors_shortestEdge, width=1, alpha=0.7)

    # Dibujar las etiquetas de las aristas
    nx.draw_networkx_edge_labels(g, posNX, edge_labels=edge_labels, font_color='black')
    
    # Agregar el canvas al lado derecho
    canvas = FigureCanvasTkAgg(plt.gcf(), master=right_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)



def clearRows(list):
    for row in list:
        widgets = left_frame.grid_slaves(row=row)
        for widget in widgets:
            widget.grid_forget()
            
    for widget in right_frame.winfo_children():
        widget.destroy()

def printRoute(graph, origin, destination, visa, pathType):  
    clearRows([4,5,6,7,8])
    if(origin.get() != "" and destination.get() != "" and visa.get() != "" and pathType.get() != ""):
        startNode = origin.get()
        end_node = destination.get()
        
        path = pathType.get()
        
        if visa.get() == "Si":
            hasVisa = True
        elif visa.get() == "No":
            hasVisa = False
                
        try:
            if path == "Ruta con menos paradas":
                shortest_distance, shortest_path = graph.findShortestStopPath(startNode, end_node, hasVisa)
                
                finalPath = ""
                index = 1
                scales = len(shortest_path)
                
                for node in shortest_path:
                    if index < scales:
                        finalPath += node + " ---> " 
                        index += 1
                    else:
                        finalPath += node
                        
                drawGraphNX(graph, shortest_path)
                
                result = ttk.Label(left_frame, text="¡Ruta generada!", font=("Arial", 14), background="orange")
                result.grid(row=4, column=0, columnspan=4, pady=10)
                country = ttk.Label(left_frame, text=finalPath, font=("Arial", 14), background="orange")
                country.grid(row=5, column=0, columnspan=4, pady=5)
                stops = ttk.Label(left_frame, text="Número de escalas: "+ str(scales-2), font=("Arial", 14), background="orange")
                stops.grid(row=6, column=0, columnspan=4, pady=5)
                cost = ttk.Label(left_frame, text="Costo total: "+str(shortest_distance), font=("Arial", 14), background="orange")
                cost.grid(row=7, column=0, columnspan=4, pady=5)
                
                
            elif path == "Ruta más barata":
                shortest_distance, shortest_path = graph.findShortestPath(startNode, end_node, hasVisa)
                
                finalPath = ""
                index = 1
                scales = len(shortest_path)
                
                for node in shortest_path:
                    if index < scales:
                        finalPath += node + " ---> " 
                        index += 1
                    else:
                        finalPath += node
                        
                drawGraphNX(graph, shortest_path)
                
                result = ttk.Label(left_frame, text="¡Ruta generada!", font=("Arial", 14), background="orange")
                result.grid(row=4, column=0, columnspan=4, pady=10)
                country = ttk.Label(left_frame, text=finalPath, font=("Arial", 14), background="orange")
                country.grid(row=5, column=0, columnspan=4, pady=5)
                stops = ttk.Label(left_frame, text="Número de escalas: "+ str(scales-2), font=("Arial", 14), background="orange")
                stops.grid(row=6, column=0, columnspan=4, pady=5)
                cost = ttk.Label(left_frame, text="Costo total: "+str(shortest_distance), font=("Arial", 14), background="orange")
                cost.grid(row=7, column=0, columnspan=4, pady=5)
            
        except ValueError:
            errorDialog()
    else:
        validateDialog()


def validateDialog():
    messagebox.showerror("Error", "Asegurese de rellenar todos los campos.")


def errorDialog():
    messagebox.showerror("Error", "No cuenta con la Visa para viajar.")


def start(graph: Graph):
    global interface, right_frame, left_frame
   # Crear la ventana principal
    interface = tk.Tk()
    interface.title("MetroTravel")
    interface.configure(bg="orange")

    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 12), background="orange")
    style.configure("TButton", font=("Arial", 12))
    style.configure("TFrame", background="orange")

    # Lado izquierdo
    left_frame = ttk.Frame(interface, style="TFrame")
    left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Título centrado
    title = ttk.Label(left_frame, text="Bienvenido a MetroTravel", font=("Arial", 20), background="orange")
    title.grid(row=0, column=0, columnspan=4, pady=10)

    originsLabel = ttk.Label(left_frame, text="País de Origen:", style="TLabel")
    originsLabel.grid(row=1, column=0, padx=10, sticky="w")
    origins = originsList(graph)
    origin = ttk.Combobox(left_frame, values=origins)
    origin.grid(row=2, column=0, padx=10)

    destinationLabel = ttk.Label(left_frame, text="País de Destino:", style="TLabel")
    destinationLabel.grid(row=1, column=1, padx=10, sticky="w")
    destinations = destinationsList(graph)
    destination = ttk.Combobox(left_frame, values=destinations)
    destination.grid(row=2, column=1, padx=10)

    visaLabel = ttk.Label(left_frame, text="¿Cuenta con Visa?:", style="TLabel")
    visaLabel.grid(row=1, column=2, padx=10, sticky="w")
    visa = ttk.Combobox(left_frame, values=["Si", "No"])
    visa.grid(row=2, column=2, padx=10)

    pathLabel = ttk.Label(left_frame, text="Tipo de ruta:", style="TLabel")
    pathLabel.grid(row=1, column=3, padx=10, sticky="w")
    pathType = ttk.Combobox(left_frame, values=["Ruta más barata", "Ruta con menos paradas"])
    pathType.grid(row=2, column=3, padx=10)

    travel = ttk.Button(left_frame, text="Buscar...", command=lambda: printRoute(graph, origin, destination, visa, pathType), style="TButton")
    travel.grid(row=3, column=0, columnspan=4, pady=20)

    # Lado derecho
    right_frame = ttk.Frame(interface)
    right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    interface.mainloop()
