from classes.graph import Graph
from scripts.csv import *
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


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


def main():
    graph = Graph()
    getNodesData(graph)
    getEdgesData(graph)

    graph.printGraph()

    startNode = 'PTP'
    end_node = 'CCS'
    hasVisa = False

    shortest_distance, shortest_path, shortest_edge = graph.findShortestPath(
        startNode, end_node, hasVisa)

    drawGraphNX(graph, shortest_path, shortest_edge)

    print("\n")

    # draw_graph(graph.graph)
    
    # Inicio de la interfaz grafica

    # root = tk.Tk()
    # root.geometry("1600x800")
    # root.title("Hi")
    # leftBackground = '#581845'
    # darkBackground = '#892915'
    # style = ttk.Style()
    # style.configure('C.TButton', font = ('Helvetica', 12, 'bold'), foreground = darkBackground, background=darkBackground)

    # rightFrame = tk.Frame(root)
    # rightFrame.pack(side='right')

    # leftFrame = tk.Frame(root)
    # leftFrame.pack(side='left')
    # leftFrame.config(bd=15, background=leftBackground)

    # # Título
    # tk.Label(leftFrame, foreground='white', background=leftBackground, text = "Wepa", font=('Helvetica', 18, 'bold') ).pack(fill='x', pady=15)
    
    # # String donde va el dato de donde comienza
    # startingPoint = tk.StringVar()
    # startingPoint.set("")
    # # String donde va el dato de a donde quiere llegar
    # arrivingPoint = tk.StringVar()
    # arrivingPoint.set("")
    # # String donde va si tiene visa o no
    # tk.Label(leftFrame, foreground='white', background=leftBackground, text = "Punto de Partida", font=('Helvetica', 12, 'bold') ).pack(fill='x',pady=15)
    # tk.Entry(leftFrame, highlightthickness=0, disabledbackground="white", disabledforeground=darkBackground, state='normal', font=('Helvetica', 12), textvariable=startingPoint, justify='center').pack(fill='x', pady=15)
    # tk.Label(leftFrame, foreground='white', background=leftBackground, text = "Punto de Llegada", font=('Helvetica', 12, 'bold') ).pack(fill='x', pady=15)
    # tk.Entry(leftFrame, highlightthickness=0, disabledbackground="white", disabledforeground=darkBackground, state='normal', font=('Helvetica', 12), textvariable=arrivingPoint, justify='center').pack(fill='x', pady=15)
    
    # tk.Label(leftFrame, foreground='white', background=leftBackground, text = "Posee Visa?", font=('Helvetica', 12, 'bold') ).pack(fill='x', pady=15)
    # combo = ttk.Combobox(leftFrame, state="readonly", values=["Si tengo Visa", "No tengo Visa"], width='100', font=('Helvetica', 14))
    # combo.set(combo["values"][0])
    # combo.pack(fill='x', pady=15)
    
    # ttk.Button(leftFrame, text="Comenzar", command = lambda: draw_graph(graph.graph), padding=15, style='C.TButton').pack(fill='x', pady=15)
    # f = plt.Figure(figsize=(7, 7), dpi=100)
    # canvas = FigureCanvasTkAgg(f, rightFrame)
    # canvas.get_tk_widget().pack()
    # root.mainloop()

    

    # shortest_stop_path = graph.findShortestStopPath(
    #     startNode, end_node, hasVisa)

    # print(
    #     f"La menor cantidad de escalas desde {startNode} hasta {end_node} es: {len(shortest_stop_path) - 2}")
    # print(f"El camino con menor cantidad de escalas es: {shortest_stop_path}")

    # Crear el objeto de grafo


if __name__ == '__main__':
    main()
