import numpy as np
import copy

def get_graph_order(adj_matrix):
    if len(adj_matrix) != len(adj_matrix[0]):
        return -1
    else:
        return len(adj_matrix)

def get_degree_sequence(adj_matrix):
    degree_sequence = []
    for vertex in range(len(adj_matrix)):
        degree_sequence.append(sum(adj_matrix[vertex]))
    degree_sequence.sort(reverse=True)
    return degree_sequence

def mapping(adj_matrix, pi):
    a = copy.deepcopy(adj_matrix)
    i = 0
    for vertice in a:
        original = copy.deepcopy(vertice)
        for j in range(len(vertice)):
            vertice[j] = original[pi[j]]
    b = copy.deepcopy(a)
    for i in range(len(a)):
        a[i] = b[pi[i]]
    return a

def convert_edges_to_adj_matrix(edges):
    adj_matrix = []
    for i in range(len(edges)):
        adj_matrix.append([])
        for j in range(len(edges)):
            if i == j:
                adj_matrix[i].append(0)
            elif (i, j) in edges or (j, i) in edges:
                adj_matrix[i].append(1)
            else:
                adj_matrix[i].append(0)
    return adj_matrix

def convert_adj_matrix_to_edges(adj_matrix):
    edges = []
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if adj_matrix[i][j] == 1 and (j, i) not in edges:
                edges.append((i, j))
    return edges