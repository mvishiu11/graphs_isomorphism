import graph_utils as utils
import numpy as np
import networkx as nx

class Graph:

    graph_counter = 0

    def __init__(self, ) -> None:
        self.edges = []
        self.vertices = []
        self.adj_matrix = []
        Graph.graph_counter += 1
        self.graph_id = Graph.graph_counter
    
    def get_graph_order(self):
        if len(self.adj_matrix) != len(self.adj_matrix[0]):
            return -1
        else:
            return len(self.adj_matrix)
    
    def get_degree_sequence(self):
        degree_sequence = []
        for vertex in range(len(self.adj_matrix)):
            degree_sequence.append(sum(self.adj_matrix[vertex]))
        degree_sequence.sort(reverse=True)
        return degree_sequence

    def __str__(self) -> str:
        return str(self.edges)

    def __repr__(self) -> str:
        return str(self.edges)
    
    def __eq__(self, other) -> bool:
        return np.array_equal(self.adj_matrix, other.adj_matrix)

    @staticmethod
    def init_with_edges(edges_list):
        graph = Graph()
        graph.edges = edges_list
        graph.vertices = list(set([item for t in edges_list for item in t]))
        graph.adj_matrix = utils.convert_edges_to_adj_matrix(edges_list)
        return graph

    @staticmethod
    def init_with_adj_matrix(adj_matrix):
        graph = Graph()
        graph.adj_matrix = adj_matrix
        graph.vertices = list(range(len(adj_matrix)))
        graph.edges = utils.convert_adj_matrix_to_edges(adj_matrix)
        return graph
    
    def to_nx_graph(self) -> nx.Graph:
        G = nx.Graph(self.edges)
        return G