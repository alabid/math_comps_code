'''
By Daniel Alabi.
Adjacency matrix implementation of a graph. 
'''

import numpy

class Graph:
    def __init__(self, n):
        self.num_vertices = n
        self.matrix = [[0]*n for i in range(n)]
        
    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    def determinant(self):
        return numpy.linalg.det(self.matrix)

    def determinant_times_2(self):
        return 2 * self.determinant()

g = Graph(3)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
print g.determinant()
