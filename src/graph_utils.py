import copy


class graph_utils:
    """
    This file contains functions that are used to manipulate graphs.

    Functions:
        get_graph_order(adj_matrix) - returns the order of the graph
        get_degree_sequence(adj_matrix) - returns the degree sequence of the graph
        mapping(adj_matrix, pi) - returns the mapping of the graph as an adjacency matrix
        convert_edges_to_adj_matrix(edges) - converts the graph from edges to adjacency matrix
        convert_adj_matrix_to_edges(adj_matrix) - converts the graph from adjacency matrix to edges
        get_vertices(edges) - returns the vertices of the graph
        edge_normalization(edges, vertices) - returns the normalized (0, len(vertices)) edges of the graph
    """
    def get_graph_order(adj_matrix):
        if len(adj_matrix) == 0:
            return 0
        if len(adj_matrix) != len(adj_matrix[0]):
            return -1
        else:
            return len(adj_matrix)

    def get_degree_sequence(adj_matrix):
        degree_sequence = []
        if len(adj_matrix) == 0:
            return degree_sequence
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

    def convert_edges_to_adj_matrix(edges, vertices):
        adj_matrix = []
        if len(edges) == 0:
            return adj_matrix
        for i in range(len(vertices)):
            adj_matrix.append([])
            for j in range(len(vertices)):
                if i == j:
                    adj_matrix[i].append(0)
                elif (vertices[i], vertices[j]) in edges or (vertices[j], vertices[i]) in edges:
                    adj_matrix[i].append(1)
                else:
                    adj_matrix[i].append(0)
        return adj_matrix

    def convert_adj_matrix_to_edges(adj_matrix):
        edges = []
        if len(adj_matrix) == 0:
            return edges
        for i in range(len(adj_matrix)):
            for j in range(len(adj_matrix)):
                if adj_matrix[i][j] == 1 and (j, i) not in edges:
                    edges.append((i, j))
        return edges

    def get_vertices(edges):
        vertices = []
        for edge in edges:
            if edge[0] not in vertices:
                vertices.append(edge[0])
            if edge[1] not in vertices:
                vertices.append(edge[1])
        return vertices

    def edge_normalization(edges, vertices):
        new_edges = []
        for eidx, edge in enumerate(edges):
            new_edges.append([0, 0])
            if edge[0] in vertices:
                new_edges[eidx][0] = vertices.index(edge[0])
            if edge[1] in vertices:
                new_edges[eidx][1] = vertices.index(edge[1])
        return new_edges