from graph import Graph

def graph_parser(filename: str):

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

# if __name__ == "__main__":
#     g1, g2 = graph_parser("C:\\Users\\jakub\\Desktop\\New Dokument tekstowy.txt")
#     print(f"Graph 1: {g1} \nGraph 2: {g2}")