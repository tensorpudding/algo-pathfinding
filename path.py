#!/usr/bin/python3

import math

def h(v1, d):
    """
    Sample heuristic function, using Euclidean distance to target
    """
    return math.sqrt((v1.x-d.x)**2 + (v1.y-d.y)**2)

class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Graph:
    def __init__(self):
        self.V = []
        self.E = {}
    def add_vertex(self, v):
        self.V.append(v)
        self.E[v] = []
    def add_edge(self, e):
        v1, v2 = e
        self.E['v1'].append('v2')
        self.E['v2'].append('v2')

def shortest-path(g, s, d):
    """
    Perform single-pair shortest path: return the shortest path in a graph g between s and d
    """
    pass