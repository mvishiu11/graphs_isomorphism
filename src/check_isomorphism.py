import sys
import argparse
from graph import Graph
from graph_utils import graph_utils as utils
from brute_force import brute_force_isomorphism_test
from graph_parser import graph_parser
from visualize import Visualize as vis

parser = argparse.ArgumentParser(description="This script is used to test if two graphs are isomorphic.")
parser.add_argument("--input_type", type=str, default="default", help="Type of input. Can be either 'default', 'edges' or 'from_file'.")
parser.add_argument("--input_file", type=str, default="..\\data.txt", help="Path to the file containing the graphs. Used only if input_type is 'from_file'. Proper formatting is required and can be seen in data.txt.")
parser.add_argument("--visualize", action="store_true", help="If specified, the graphs will be visualized and saved as html files.")
args = parser.parse_args()

if __name__ == "__main__":
    
    g1 = Graph()
    g2 = Graph()

    # Input type option - check if the input type is valid, if not, use default
    
    # Default option, use default graphs
    if(args.input_type == "default"):        
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

        g1 = Graph.init_with_edges(edges)
        g2 = Graph.init_with_adj_matrix(AG2)
        print(f"Those graphs are isomorphic: {brute_force_isomorphism_test(g1, g2)}!")


    # Manual edges option, use manually entered edges to create graphs
    if(args.input_type == "edges"):
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
    
    # Input graphs from file with proper formatting
    if(args.input_type == "from_file"):
        filename = "..\\data.txt"
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

    # Visualize option - create html files with graphs with pyvis
    if(args.visualize):
        vis.visualize_graph(g1)
        vis.visualize_graph(g2)