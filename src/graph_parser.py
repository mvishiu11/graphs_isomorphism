from graph import Graph


def graph_parser(filename: str):
    """
    Graph parser - parse the graph from the file with proper formatting.

    Parameters:
        filename : str - path to the file with graph

    Expected formatting of the file:
        First line: "edges" or "adj_matrix" - type of the input
        Double newline
        One or more lines: graph 1 - edges or adjacency matrix, written in a pythonic convention
        Double newline
        One or more lines: graph 2 - edges or adjacency matrix, written in a pythonic convention

    Returns:
        g1 : Graph - first graph
        g2 : Graph - second graph
    """

    g1 = Graph()
    g2 = Graph()
    with open(filename, "r") as f:
        content = f.read()
        content = content.split("\n\n")
        graph1_content = eval(content[1])
        graph2_content = eval(content[2])
        
        if content[0] == "edges":
            g1 = Graph.init_with_edges(graph1_content)
            g2 = Graph.init_with_edges(graph2_content)
        
        elif content[0] == "adj_matrix":
            g1 = Graph.init_with_adj_matrix(graph1_content)
            g2 = Graph.init_with_adj_matrix(graph2_content)
        
        else:
            raise NotImplementedError(f"The input type: {content[0]} is not supported!")
    
    f.close()
    return g1, g2

# Testing function - uncomment to test
# if __name__ == "__main__":
#     g1, g2 = graph_parser("C:\\Users\\jakub\\Desktop\\New Dokument tekstowy.txt")
#     print(f"Graph 1: {g1} \nGraph 2: {g2}")