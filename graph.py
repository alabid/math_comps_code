'''
By Daniel Alabi.
Adjacency matrix implementation of a graph. 
'''

import numpy

class Graph:
    EDGE_EXISTS = 1
    NO_EDGE = 0
    def __init__(self, n):
        self.num_vertices = n
        self.matrix = [[0]*n for i in range(n)]
        
    def add_edge(self, i, j):
        self.matrix[i][j] = self.EDGE_EXISTS
        self.matrix[j][i] = self.EDGE_EXISTS

    def determinant(self, matrix):
        return numpy.linalg.det(matrix)

    def get_val(self, i, j):
        return "x" if self.matrix[i][j] == self.EDGE_EXISTS else "o"

    def print_graph(self):        
        print "  ",
        for i in range(len(self.matrix)):
            print str(i).center(len(self.get_val(i, i))),
        print
        for i in range(len(self.matrix)):
            print i,
            for j in range(len(self.matrix)):
                print self.get_val(i, j),
            print

def main():
    # no perfect matching here
    g1 = Graph(3)
    g1.add_edge(0, 1)
    g1.add_edge(0, 2)
    g1.add_edge(1, 2)
    g1.print_graph()

    # perfect matching here
    g2 = Graph(4)
    g2.add_edge(0, 1)
    g2.add_edge(0, 3)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    g2.print_graph()


if __name__ == "__main__":
    main()
