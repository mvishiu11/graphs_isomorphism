import networkx as nx
from graph import Graph
from pyvis.network import Network

class Visualize:
    """
    Contains methods for visualizing graphs.

    Methods:
        visualize_graph_through_nx(graph) - visualizes the graph through first converting it to networkx graph
        visualize_graph(graph) - visualizes the graph manually
    """
    def visualize_graph_through_nx(graph: Graph):
        G = graph.to_nx_graph()
        net = Network(notebook=True)
        net.from_nx(G)
        net.show("nx.html")

    def visualize_graph(graph: Graph, *graphs):
        net = Network(notebook=True)
        for edge in graph.edges:
            net.add_node(edge[0], label="Node" + str(edge[0]))
            net.add_node(edge[1], label="Node" + str(edge[1]))
            net.add_edge(edge[0], edge[1])
        net.show(f"./graph{graph.graph_id}.html")

        if graphs:
            try:
                for new_graph in graphs:
                    assert type(new_graph) is Graph
                    new_net = Network(notebook=True)
                    for edge in new_graph.edges:
                        new_net.add_node(edge[0], label="Node" + str(edge[0]))
                        new_net.add_node(edge[1], label="Node" + str(edge[1]))
                        new_net.add_edge(edge[0], edge[1])
                    net.show(f"./graph{new_graph.graph_id}.html")
            except AssertionError:
                print("Wrong input format. Visualizer only supports Graph objects.")
                exit(-1)

# Run this file to see the visualization of the graph - function used for testing
# if __name__ == "__main__":
#     edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
#     graph = Graph.init_with_edges(edges)
#     Visualize.visualize_graph(graph)