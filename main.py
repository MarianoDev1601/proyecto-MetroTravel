from interface.interface import start
from classes.graph import Graph
from scripts.csv import *
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def main():
    graph = Graph()
    getNodesData(graph)
    getEdgesData(graph)
    
    start(graph)
    
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
    
    # ttk.Button(leftFrame, text="Comenzar", command = lambda: drawGraphNX(graph.graph), padding=15, style='C.TButton').pack(fill='x', pady=15)
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
