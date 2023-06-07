from classes.graph import Graph
from scripts.csv import *


def main():
    graph = Graph()
    getNodesData(graph)
    getEdgesData(graph)
    startNode = 'PTP'
    end_node = 'CCS'

    shortest_distance, shortest_path = graph.findShortestPath(
        startNode, end_node, True)

    print(
        f"La distancia más corta desde {startNode} hasta {end_node} es: {shortest_distance}")
    print(f"El camino más corto es: {shortest_path} \n")

    shortest_stop_path = graph.findShortestStopPath(
        startNode, end_node, True)

    print(
        f"La menor cantidad de escalas desde {startNode} hasta {end_node} es: {len(shortest_stop_path) - 2}")
    print(f"El camino con menor cantidad de escalas es: {shortest_stop_path}")
    print(f"\n")


if __name__ == '__main__':
    main()
