from collections import deque
import heapq
from classes.node import Node


class Graph:
    def __init__(self):
        self.graph = {}
        self.nodes = {}

    def addEdge(self, orig: str, dest: str, cost: float):
        if orig not in self.graph:
            self.graph[orig] = []
        if dest not in self.graph:
            self.graph[dest] = []

        self.graph[orig].append((dest, cost))
        # Como es no dirigido, también se coloca al inverso
        self.graph[dest].append((orig, cost))

    def addNode(self, node: Node):
        self.nodes[node.code] = node
        if node.code not in self.graph:
            self.graph[node.code] = []

    def printGraph(self):
        for source, destination in self.graph.items():
            print(
                f"{source}-->{destination}")

    def findShortestPath(self, startNode: str, endNode: str, hasVisa: bool):
        if (not hasVisa and self.nodes[startNode].visaRequired):
            raise ValueError(
                f"Para comenzar por el nodo {startNode} se requiere de una visa.")
        if (not hasVisa and self.nodes[endNode].visaRequired):
            raise ValueError(
                f"Para llegar a el nodo {endNode} se requiere de una visa.")

        nodes = {node: {"distance": float(
            'inf'), "previous": None} for node in self.graph}

        nodes[startNode]["distance"] = 0

        visited = set()

        while True:
            currentDistance = float('inf')
            currentNode = None
            # Encontrar el nodo no visitado con la distancia mínima
            for node in self.graph:
                # Solo se pueden contemplar las islas que se puedan visitar
                if (not hasVisa and self.nodes[node].visaRequired):
                    continue

                if nodes[node]['distance'] < currentDistance and node not in visited:
                    currentDistance = nodes[node]['distance']
                    currentNode = node

            if (currentNode is None):
                break

            visited.add(currentNode)

            # Actualizar las distancias de los nodos vecinos no visitados
            for neighbor, cost in self.graph[currentNode]:
                # Solo se pueden contemplar las islas que se puedan visitar
                if (not hasVisa and self.nodes[neighbor].visaRequired):
                    continue

                distance = nodes[currentNode]['distance'] + cost

                if distance < nodes[neighbor]['distance']:
                    nodes[neighbor]['distance'] = distance
                    nodes[neighbor]['previous'] = currentNode

        if endNode not in visited:
            raise ValueError(
                "No se encontró un camino desde el nodo de inicio al nodo de destino.")

        # # Reconstruir la ruta desde el nodo de destino hasta el nodo de inicio
        path = []
        current = endNode
        while current != startNode:
            path.append(current)
            current = nodes[current]['previous']
        path.append(startNode)
        path.reverse()

        return nodes[endNode]['distance'], path

    def findShortestStopPath(self, startNode: str, endNode: str, hasVisa: bool):

        if (not hasVisa and self.nodes[startNode].visaRequired):
            raise ValueError(
                f"Para comenzar por el nodo {startNode} se requiere de una visa.")
        if (not hasVisa and self.nodes[endNode].visaRequired):
            raise ValueError(
                f"Para llegar a el nodo {endNode} se requiere de una visa.")

        # Inicializar los nodos visitados y el camino
        visited = set()
        path = []

        # Cola para almacenar los nodos a visitar
        queue = [(startNode, [])]

        while queue:
            currentNode, currentPath = queue.pop(0)

            # Solo se pueden contemplar las islas que se puedan visitar
            if (not hasVisa and self.nodes[currentNode].visaRequired):
                continue

            if currentNode == endNode:
                # Se encontró el nodo de destino, se retorna el camino
                path = currentPath + [currentNode]
                break

            if currentNode not in visited:
                visited.add(currentNode)
                for neighbor in self.graph[currentNode]:
                    queue.append((neighbor[0], currentPath + [currentNode]))

        if not path:
            # No se encontró un camino desde el nodo de inicio al nodo de destino
            raise ValueError(
                "No se encontró un camino desde el nodo de inicio al nodo de destino.")

        return path
