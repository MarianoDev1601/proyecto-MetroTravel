from classes.graph import Graph
from scripts.csv import *
import matplotlib.pyplot as plt
import numpy as np


def draw_graph(graph):
    # Crear una figura y un objeto de ejes
    fig, ax = plt.subplots()

    # Calcular el ángulo de separación entre los nodos
    num_nodes = len(graph)
    theta = 2 * np.pi / num_nodes

    # Asignar posiciones en el eje x a cada nodo
    positions = {node: (np.cos(i * theta), np.sin(i * theta))
                 for i, node in enumerate(graph)}

    # Dibujar los nodos como puntos en el gráfico
    for node, position in positions.items():
        ax.scatter(position[0], position[1], color='blue')
        ax.annotate(node, position, textcoords="offset points",
                    xytext=(0, 10), ha='center')

    # Dibujar las aristas entre los nodos
    for node, neighbors in graph.items():
        x1, y1 = positions[node]
        for neighbor, cost in neighbors:
            x2, y2 = positions[neighbor]
            ax.plot([x1, x2], [y1, y2], color='black')

    # Establecer los límites del gráfico
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])

    # Mostrar el gráfico
    plt.show()


def main():
    graph = Graph()
    getNodesData(graph)
    getEdgesData(graph)

    graph.printGraph()

    print("\n")

    draw_graph(graph.graph)
    # startNode = 'PTP'
    # end_node = 'CCS'

    # shortest_distance, shortest_path = graph.findShortestPath(
    #     startNode, end_node, True)

    # print(
    #     f"La distancia más corta desde {startNode} hasta {end_node} es: {shortest_distance}")
    # print(f"El camino más corto es: {shortest_path} \n")

    # shortest_stop_path = graph.findShortestStopPath(
    #     startNode, end_node, True)

    # print(
    #     f"La menor cantidad de escalas desde {startNode} hasta {end_node} es: {len(shortest_stop_path) - 2}")
    # print(f"El camino con menor cantidad de escalas es: {shortest_stop_path}")


if __name__ == '__main__':
    main()
