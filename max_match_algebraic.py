from graph import Graph
from random import randint
import numpy as np

class TutteGraph(Graph):
    BIG_NUM = 10000
    def __init__(self, n):
        Graph.__init__(self, n)

    def add_edge(self, i, j):
        self.matrix[i][j] = self.get_indeterminate(i, j)
        self.matrix[j][i] = self.get_indeterminate(j, i)
    
    def get_indeterminate(self, i, j):
        val = self.BIG_NUM*i + j
        return val if i < j else -val

    def get_val(self, i, j):
        val = abs(self.matrix[i][j])
        if val > 0:
            u = val / self.BIG_NUM
            v = val % self.BIG_NUM
        else:
            u = i
            v = j
            
        if self.matrix[i][j] > 0:
            return "|  X(%2d, %2d)" % (u, v) 
        elif self.matrix[i][j] < 0:
            return "| -X(%2d, %2d)" % (v, u)
        else:
            return "|" + "0".center(11)
        
    def empty_matrix(self):
        n = self.num_vertices
        return [[0]*n for i in range(n)]

    def get_adj_matrix(self):
        matrix = self.empty_matrix()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                matrix[i][j] = 1 if self.matrix[i][j] != 0 else 0
        return matrix

    def get_tutte_matrix(self, m = None):
        m = self.num_vertices**2 if m == None else m
        matrix = self.empty_matrix()

        for i in range(len(self.matrix)):
            for j in range(i+1, len(self.matrix)):
                if self.matrix[i][j] != 0:
                    random_num = randint(1, m)
                    matrix[i][j] = random_num
                    matrix[j][i] = -random_num
        return matrix

    # algorithm by Lovasz
    def rand_has_perfect_matching(self, times = 1):
        for i in range(times):
            result = round(abs(self.determinant(self.get_tutte_matrix())),
                           10) > 0
            if result:
                return True
        return False

    def empty(self, graph_matrix):
        for i in range(len(graph_matrix)):
            for j in range(len(graph_matrix)):
                if graph_matrix[i][j] == 1:
                    return False
        return True

    def inverse(self, matrix):
        return np.linalg.inv(matrix)

    def find_next_edge(self, graph_matrix, inv_tutte_matrix):
        for i in range(len(graph_matrix)):
            for j in range(len(graph_matrix)):
                if graph_matrix[i][j] == 1 and round(inv_tutte_matrix[i][j],
                                                     10) != 0:
                    return (i,j)
        return None

    def delete_edge(self, graph_matrix, edge):
        u = edge[0]
        v = edge[1]

        for i in range(len(self.matrix)):
            graph_matrix[u][i] = 0
            graph_matrix[i][u] = 0
            graph_matrix[v][i] = 0
            graph_matrix[i][v] = 0


    def rank(self, matrix):
        return np.linalg.matrix_rank(matrix)

    # Rabin-Vazirani algorithm for computing maximum matching
    def get_max_matching(self):
        max_matching = []
        graph_matrix = self.get_adj_matrix()
        print self.rank(self.matrix)
        while not self.empty(graph_matrix):
            tutte_matrix = self.get_tutte_matrix()            
            try:
                inv_tutte_matrix = self.inverse(tutte_matrix)
            except np.linalg.linalg.LinAlgError:
                return "This graph does not have a perfect matching"

            new_edge = self.find_next_edge(graph_matrix, inv_tutte_matrix)
            if new_edge == None:
                break
            (i, j) = new_edge
                
            max_matching.append(new_edge)
            self.delete_edge(graph_matrix, (i,j))

        return max_matching
    
def main():
    # no perfect matching here
    g1 = TutteGraph(3)
    g1.add_edge(0, 1)
    g1.add_edge(0, 2)
    g1.add_edge(1, 2)
    g1.print_graph()
    print "G1 have perfect matching?", g1.rand_has_perfect_matching(100)
    print "G1 max matching set:", g1.get_max_matching()

    # perfect matching here
    g2 = TutteGraph(4)
    g2.add_edge(0, 1)
    g2.add_edge(0, 3)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    g2.print_graph()
    print "G2 have perfect matching?", g2.rand_has_perfect_matching(100)
    print "G2 max matching set:", g2.get_max_matching()

'''
Questions:
1. When will the algorithm say that it has a perfect matching when it 
   doesn't?
2. When will the algorithm say that it doesn't have a perfect matching
   when it does?
3. How can you make it faster?
Theorems? Proofs?

'''

if __name__ == "__main__":
    main()
