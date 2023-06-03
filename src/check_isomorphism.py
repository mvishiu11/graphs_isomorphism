import sys
from graph import Graph
import graph_utils as utils
from brute_force import brute_force_isomorphism_test
from graph_parser import graph_parser
from visualize import visualize_graph

if __name__ == "__main__":
    
    g1 = Graph()
    g2 = Graph()

    if("--help" in sys.argv):
            print("""
            This script is used to test if two graphs are isomorphic.
            The input can be given either by specifying edges of the graph or providing adjacency matrix.

            The graphs can be entered either manually or from a file.
            The input type is specified by the "--input_type" argument.
            The input file is specified by the "--input_file" argument.

                Usage: python3 isomorphism_test.py --input_type <input_type> --input_file <input_file> --visualize
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

            If you want to visualize the graphs, use the "--visualize". 
            The graphs will be saved in the base directory of this app as html files.
            """)
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

        g1 = Graph.init_with_edges(edges)
        g2 = Graph.init_with_adj_matrix(AG2)
        print(f"Those graphs are isomorphic: {brute_force_isomorphism_test(g1, g2)}!")

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

    visualize = False
    if("--visualize" in sys.argv):
        visualize = True

    if(visualize):
        visualize_graph(g1)
        visualize_graph(g2)