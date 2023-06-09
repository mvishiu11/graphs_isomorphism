import itertools
import numpy as np
from graph_utils import graph_utils as utils
from graph import Graph
from math import factorial
import tqdm
import time

def brute_force_isomorphism_test(g1 : Graph, g2 : Graph) -> bool:
    """
    Brute force isomorphism test - check if two graphs are isomorphic by checking all possible mappings of the 
    first graph to the second graph. If one of the mappings is equal to the second graph, return True, otherwise
    retrun False.

    Parameters:
        g1 : Graph - first graph
        g2 : Graph - second graph

    Returns:
        bool - True if the graphs are isomorphic, False otherwise
    """
    degree_sequence_1 = g1.get_degree_sequence()
    degree_sequence_2 = g2.get_degree_sequence()
    if g1.get_graph_order() != g2.get_graph_order():
        return False
    elif not np.array_equal(degree_sequence_1, degree_sequence_2):
        return False
    else:
        perms = itertools.permutations([obj[0] for obj in enumerate(g1.vertices)])
        len_perms = factorial(len(g1.vertices))
        iteration = 0
        
        if(len(g1.vertices) > 9):
            for map in tqdm.tqdm(perms, total=len_perms):
                if(np.array_equal(utils.mapping(g1.adj_matrix, map), g2.adj_matrix)):
                    print(f"Number of iterations until convergence: {iteration}")
                    return True
                else:
                    continue
            return False
        
        else:
            for map in perms:
                if(np.array_equal(utils.mapping(g1.adj_matrix, map), g2.adj_matrix)):
                    return True
                else:
                    continue
            return False