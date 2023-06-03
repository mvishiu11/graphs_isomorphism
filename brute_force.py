import itertools
import numpy as np
import graph_utils as utils
from graph import Graph
import sys
from graph_parser import graph_parser

# AG1 =  [[0, 1, 0, 0, 1], 
#         [1, 0, 1, 0, 0],
#         [0, 1, 0, 1, 0],
#         [0, 0, 1, 0, 1],
#         [1, 0, 0, 1, 0]]
        
# AG2 =  [[0, 0, 1, 1, 0], 
#         [0, 0, 0, 1, 1],
#         [1, 0, 0, 0, 1],
#         [1, 1, 0, 0, 0],
#         [0, 1, 1, 0, 0]]

def brute_force_isomorphism_test(g1 : Graph, g2 : Graph) -> bool:
    degree_sequence_1 = g1.get_degree_sequence()
    degree_sequence_2 = g2.get_degree_sequence()
    if g1.get_graph_order() != g2.get_graph_order():
        return False
    elif not np.array_equal(degree_sequence_1, degree_sequence_2):
        return False
    else:
        for map in itertools.permutations(g1.vertices):
            if(np.array_equal(utils.mapping(g1.adj_matrix, map), g2.adj_matrix)):
                return True
            else:
                continue
        return False

if __name__ == "__main__":

    if("--help" in sys.argv):
        print("""This script is used to test if two graphs are isomorphic.
            The input can be given either by specifying edges of the graph or providing adjacency matrix.

            The graphs can be entered either manually or from a file.
            The input type is specified by the "--input_type" argument.
            The input file is specified by the "--input_file" argument.

            Usage: python3 isomorphism_test.py --input_type <input_type> --input_file <input_file>
                                                            edges                     ".\\data.txt"
                                                            from_file                 <your_file_path>  
                                                            default    
              
            If you are using a file input, it should be in the following format:
              
              <file_begin>
              input_type (edges/adj_matrix) \\n\\n (double new line)
              graph1 content \\n\\n (double new line)
              graph2 content
              <file_end>

            Precise formatting can be seen in the provided data.txt file.
              """)
        exit(0)

    if "--version" in sys.argv:
        print("Version 0.1")
        exit(0)

    input_type = "default"
    if("--input_type" in  sys.argv):
        input_type = sys.argv[sys.argv.index("--input_type") + 1]

    if(input_type == "default"):        
        edges = [(0, 1), (0, 4), (1, 2), (2, 3), (3, 4)]
        AG2 =  [[0, 0, 1, 1, 0], 
                [0, 0, 0, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 0, 0, 0],
                [0, 1, 1, 0, 0]]
        
        print(f"""Using default graphs: 
              Graph 1:  {edges}
              Graph 2:  {utils.convert_adj_matrix_to_edges(AG2)}
              """)

        g = Graph.init_with_edges(edges)
        g2 = Graph.init_with_adj_matrix(AG2)
        print(f"Those graphs are isomorphic: {brute_force_isomorphism_test(g, g2)}!")

    if(input_type == "edges"):
        edges1 = []
        edges2 = []
        print("""The edges should be entered as follows:

              (a, b), where (a, b) is an edge between a and b; a, b being integers. Enter "end" to stop entering edges.\n""")

        print("Enter edges for graph 1:")
        while(True):
            edge = input("\t: ")
            if(edge == "end"):
                break
            edges1.append(eval(edge))
        print("Enter edges for graph 2: ")
        while(True):
            edge = input("\t: ")
            if(edge == "end"):
                break
            edges2.append(eval(edge))
        g1 = Graph.init_with_edges(edges1)
        g2 = Graph.init_with_edges(edges2)
        print(f"Graph 1: {g1} \nGraph 2: {g2}")
        print(f"Those graphs are isomorphic: {brute_force_isomorphism_test(g1, g2)}!")
    
    if(input_type == "from_file"):
        filename = ".\\data.txt"
        if("--input_file" in sys.argv):
            filename = sys.argv[sys.argv.index("--input_file") + 1]

        try:
            g1, g2 = graph_parser(filename)
        except NotImplementedError as e:
            print("Error while parsing the file. Please check the file format.")
            print(e.args[0])
            exit(1)
        print(f"Graph 1: {g1} \nGraph 2: {g2}")
        print(f"Those graphs are isomorphic: {brute_force_isomorphism_test(g1, g2)}!")