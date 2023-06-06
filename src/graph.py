from graph_utils import graph_utils as utils
import numpy as np
import networkx as nx


class Graph:
    """
    Class representing a graph. It can be initialized with edges or adjacency matrix.

    Attributes:
        edges : list - list of edges
        vertices : list - list of vertices
        adj_matrix : list[list] - adjacency matrix
        graph_id : int - unique id of the graph
        graph_counter : int - counter of the instances of the class

    Methods:
        get_graph_order() - returns the order of the graph
        get_degree_sequence() - returns the degree sequence of the graph
        __str__() - returns the string representation of the graph
        __repr__() - returns the string representation of the graph
        __eq__() - returns True if the graphs are equal, False otherwise
        init_with_edges(edges_list) - initializes the graph with edges
        init_with_adj_matrix(adj_matrix) - initializes the graph with adjacency matrix
        to_nx_graph() - returns the networkx graph representation of the graph
    """

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

    def normalize_edges(self):
        return utils.edge_normalization(self.edges, self.vertices)

    def add_edge(self, edge) -> None:
        if edge not in self.edges: 
            self.edges.append(edge)
            self.vertices = utils.get_vertices(self.edges)
            self.adj_matrix = utils.convert_edges_to_adj_matrix(self.edges, self.vertices)

    @staticmethod
    def init_with_edges(edges_list):
        graph = Graph()
        for edge in edges_list:
            graph.add_edge(edge)
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