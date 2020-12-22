
class my_graph:
    def __init__(self,graph_dict):
        self.graph_dict = graph_dict
    def is_edge(self,v1,v2):
        if ( not (isinstance(v1, str)) or not (isinstance(v2, str)) or (v1 not in self.graph_dict.keys()) or (v2 not in self.graph_dict.keys()) or (v1 == v2) ):
            raise ValueError("Incorrect, same or missing vertex.")
        return v2 in self.graph_dict[v1]
    def list_edges(self):
        explored_vertices = set()
        vertex_pairs = set()
        def explore(v1):
            explored_vertices.add(v1)
            for v2 in self.graph_dict[v1]:
                if v2 not in explored_vertices:
                    vertex_pairs.add((v1,v2))
                    explore(v2)
                else:
                    if (v1,v2) not in vertex_pairs and (v2,v1) not in vertex_pairs:
                        vertex_pairs.add((v1,v2))
                    return
        for v in self.graph_dict.keys():
            if v not in explored_vertices:
                 explore(v)
            else:
                continue
        return vertex_pairs
    def list_neighbors(self,v1):
        if (v1 not in self.graph_dict.keys()):
            raise ValueError("Incorrect, same or missing vertex.")
        return self.graph_dict[v1]
    def path(self,v1,v2):
        return self.is_edge(v1,v2)
    def connected_components(self):
        explored_vertices = set()
        connected_components_list = []
        def explore(v1):
            explored_vertices.add(v1)
            connected_component.add(v1)
            for v2 in self.graph_dict[v1]:
                if v2 not in explored_vertices:
                    explore(v2)
                else:
                    return
        for v in self.graph_dict.keys():
            connected_component = set()
            if v not in explored_vertices:
                 explore(v)
            else:
                continue
            connected_components_list.append(connected_component)
        return connected_components_list
    def __str__(self):
        return str (self.graph_dict)


if __name__ == '__main__':
    my_test_graph = my_graph({"A":{"B","C"},"B":{"A","C"},"C":{"A","B"},"D":{"E"},"E":{"D"},"F":{"G"},"G":{"F"}})
    print(my_test_graph.connected_components())