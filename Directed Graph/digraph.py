
from collections import deque
from queue import PriorityQueue

class my_digraph:
    def __init__(self,graph_dict):
        self.graph_dict = graph_dict
        self.number_vertices = 0
        for v in self.graph_dict.keys():
            self.number_vertices += len(self.graph_dict[v])
    def __str__(self):
        return str (self.graph_dict)
    def number_vertices(self):
        return self.number_vertices
    def bellman_ford(self,v1,v2):
        bf_dict = {}
        parent_dict = {}
        for v in self.graph_dict.keys():
            bf_dict[v] = None
            parent_dict[v] = None
        bf_dict[v1] = 0
        parent_dict[v1] = 0
        breadth_first_search_list = []
        breadth_first_search_set = set()
        def bfs_build_que(v):
            if v not in breadth_first_search_set:
                breadth_first_search_list.append(v)
                breadth_first_search_set.add(v) 
            for vertex in self.graph_dict[v]:                  
                if vertex not in breadth_first_search_set:
                    breadth_first_search_list.append(vertex)
                    breadth_first_search_set.add(vertex)
        for v in self.graph_dict.keys():
            bfs_build_que(v)
        for index in range(0,self.number_vertices-1):
            for vertex in breadth_first_search_list:
                vertex_cost = bf_dict[vertex]
                if vertex_cost == None:
                    continue
                for vertex2 in self.graph_dict[vertex]:
                    if bf_dict[vertex2] == None or bf_dict[vertex2] > vertex_cost +  self.graph_dict[vertex][vertex2][0]:
                        bf_dict[vertex2] = vertex_cost +  self.graph_dict[vertex][vertex2][0]
                        parent_dict[vertex2] = vertex
        return parent_dict
    def dijkstra(self,v1,v2):
        priority_que = PriorityQueue()
        visited =  set()
        bf_dict = {}
        parent_dict = {}
        for v in self.graph_dict.keys():
            bf_dict[v] = None
            parent_dict[v] = None
        bf_dict[v1] = 0
        parent_dict[v1] = 0
        priority_que.put((0,v1))
        while not priority_que.empty():
            curr_node = priority_que.get()[1]
            if curr_node not in visited:
                visited.add(curr_node)
                if curr_node == v2:
                    return parent_dict
                for item in self.graph_dict[curr_node]:
                    vertex_cost = bf_dict[curr_node]
                    #if path from curr to item is shorter
                    if bf_dict[item] == None or bf_dict[item] > vertex_cost + self.graph_dict[curr_node][item][0]:
                        bf_dict[item] = vertex_cost + self.graph_dict[curr_node][item][0]
                        parent_dict[item] = curr_node
                        priority_que.put((vertex_cost + self.graph_dict[curr_node][item][0], item))
    def __str__(self):
        return str (self.graph_dict)

if __name__ == '__main__':
    my_test_graph = my_digraph({"A":{"B":(2,)},"B":{"C":(2,)},"C":{"A":(12,)}})
    my_test_graph.dijkstra("A","C")
    my_test_graph.bellman_ford("A","C")