import unittest
import random
from graph import my_graph

class test_graph(unittest.TestCase):
    def setUp(self):
        print('\n Run setup...')
    def tearDown(self):
        print('\n Run teardown...')
        pass
    def test_is_edge_on_conncted_vertices_returns_true(self):
        print('check if the given two vertices are conncted via an edge. This test should return true...')
        self.my_test_graph = my_graph({"A":{"B","C"},"B":{"A","C"},"C":{"A","B"},"D":{"E"},"E":{"D"}})
        print(self.my_test_graph)
        self.assertEqual(self.my_test_graph.is_edge("A","B"),True)
    def test_is_edge_on_conncted_vertices_returns_false(self):
        print('check if the given two vertices are conncted via an edge. This test should return false...')
        self.my_test_graph = my_graph({"A":{"B","C"},"B":{"A","C"},"C":{"A","B"},"D":{"E"},"E":{"D"}})
        print(self.my_test_graph)
        self.assertEqual(self.my_test_graph.is_edge("A","E"),False)
    def test_is_edge_throws_error_if_type_of_vertex_arguemnt_is_not_string(self):
        print('If you provide a non-string argument to is edge function should raise an error ...')
        self.my_test_graph = my_graph({"A":{"B","C"},"B":{"A","C"},"C":{"A","B"},"D":{"E"},"E":{"D"}})
        print(self.my_test_graph)
        self.assertRaises(ValueError,self.my_test_graph.is_edge,"A",2)
        self.assertRaises(ValueError,self.my_test_graph.is_edge,2,"A")
        self.assertRaises(ValueError,self.my_test_graph.is_edge,1,2)
    def test_is_edge_throws_error_if_enough_arguments_not_provided(self):
        print('If gewers than arguments are provided should raise an error ...')
        self.my_test_graph = my_graph({"A":{"B","C"},"B":{"A","C"},"C":{"A","B"},"D":{"E"},"E":{"D"}})
        print(self.my_test_graph)
        self.assertRaises(TypeError,self.my_test_graph.is_edge,"2")
    def test_is_edge_throws_error_if_asking_for_non_existent_vertex(self):
        print('If vertex does not exist, function should raise an error ...')
        self.my_test_graph = my_graph({"A":{"B","C"},"B":{"A","C"},"C":{"A","B"},"D":{"E"},"E":{"D"}})
        print(self.my_test_graph)
        self.assertRaises(ValueError,self.my_test_graph.is_edge,"A","2")
        self.assertRaises(ValueError,self.my_test_graph.is_edge,"2","A")
        self.assertRaises(ValueError,self.my_test_graph.is_edge,"2","1")
        self.assertRaises(ValueError,self.my_test_graph.is_edge,"","B")
    def test_is_edge_throws_error_if_both_vertices_are_same(self):
        print('If both vertixes are same, function should raise an error ...')
        self.my_test_graph = my_graph({"A":{"B","C"},"B":{"A","C"},"C":{"A","B"},"D":{"E"},"E":{"D"}})
        print(self.my_test_graph)
        self.assertRaises(ValueError,self.my_test_graph.is_edge,"A","A")
    def test_list_edges(self):
        print('If check to make sure that all edges are listed ...')
        self.my_test_graph = my_graph({"A":{"B"},"B":{"A"}})
        self.my_test_graph2 = my_graph({"A":{"C"},"B":{"C"},"C":{"A","B"}})
        print(self.my_test_graph)
        self.assertTrue(self.my_test_graph.list_edges() == {('A', 'B')} or self.my_test_graph.list_edges() == {('B', 'A')})
        self.assertTrue(self.my_test_graph2.list_edges() == {('A', 'C'),('B', 'C')} or self.my_test_graph2.list_edges() == {('C', 'A'),('C', 'B')} or self.my_test_graph2.list_edges() == {('A', 'C'),('C', 'B')} or self.my_test_graph2.list_edges() == {('C', 'A'),('B', 'C')})
    def test_list_nieghbors(self):
        print('If check to make sure that all edges are listed ...')
        self.my_test_graph = my_graph({"A":{"B","C"},"B":{"A","C"},"C":{"A","B"},"D":{"E"},"E":{"D"}})
        print(self.my_test_graph)
        self.assertEqual(self.my_test_graph.list_neighbors("A"),{"B","C"})
        self.assertEqual(self.my_test_graph.list_neighbors("B"),{"A","C"})
        self.assertEqual(self.my_test_graph.list_neighbors("D"),{"E"})
    def test_if_list_neighbors_if_type_of_vertex_arguemnt_is_not_string(self):
        print('If you list neighbor argument to is edge function should raise an error ...')
        self.my_test_graph = my_graph({"A":{"B","C"},"B":{"A","C"},"C":{"A","B"},"D":{"E"},"E":{"D"}})
        print(self.my_test_graph)
        self.assertRaises(TypeError,self.my_test_graph.is_edge,"H")
        self.assertRaises(TypeError,self.my_test_graph.is_edge,"2")   
        self.assertRaises(TypeError,self.my_test_graph.is_edge,1)
        self.assertRaises(TypeError,self.my_test_graph.is_edge,[1])
        self.assertRaises(TypeError,self.my_test_graph.is_edge)
    def test_if_path_exists_between_vertices_return_true(self):
        print('check to see if path exists. Should return true ...')
        self.my_test_graph = my_graph({"A":{"B","C"},"B":{"A","C"},"C":{"A","B"},"D":{"E"},"E":{"D"}})
        print(self.my_test_graph)
        self.assertEqual(self.my_test_graph.path("A","B"),True)
        self.assertEqual(self.my_test_graph.path("B","C"),True)
        self.assertEqual(self.my_test_graph.path("C","A"),True)
        self.assertEqual(self.my_test_graph.path("C","B"),True)
        self.assertEqual(self.my_test_graph.path("C","B"),True)
        self.assertEqual(self.my_test_graph.path("D","E"),True)
    def test_if_path_exists_between_vertices_return_false(self):
        print('check to see if path exists. Should return false ...')
        self.my_test_graph = my_graph({"A":{"B","C"},"B":{"A","C"},"C":{"A","B"},"D":{"E"},"E":{"D"}})
        print(self.my_test_graph)
        self.assertEqual(self.my_test_graph.path("A","E"),False)
        self.assertEqual(self.my_test_graph.path("B","D"),False)
        self.assertEqual(self.my_test_graph.path("D","A"),False)
        self.assertEqual(self.my_test_graph.path("D","B"),False)
        self.assertEqual(self.my_test_graph.path("D","C"),False)
        self.assertEqual(self.my_test_graph.path("C","D"),False)
    def test_path_wrong_vertices_should_return_error(self):
        print('check path with wrong vertices. Should return error ...')
        self.my_test_graph = my_graph({"A":{"B","C"},"B":{"A","C"},"C":{"A","B"},"D":{"E"},"E":{"D"}})
        print(self.my_test_graph)
        self.assertRaises(ValueError,self.my_test_graph.path,[1],"A")
        self.assertRaises(ValueError,self.my_test_graph.path,"U","A")
        self.assertRaises(ValueError,self.my_test_graph.path,"A","Q")
        self.assertRaises(ValueError,self.my_test_graph.path,"A","")
        self.assertRaises(ValueError,self.my_test_graph.path,"A",1)
        self.assertRaises(TypeError,self.my_test_graph.path,"A")
    def test_connected_componenets(self):
        print('List all connected components ...')
        self.my_test_graph = my_graph({"A":{"B"},"B":{"A"}})
        self.my_test_graph2 = my_graph({"A":{"B"},"B":{"A"},"D":{"E"},"E":{"D"}})
        print(self.my_test_graph)
        self.assertTrue(self.my_test_graph.connected_components() == [{'A', 'B'}] or self.my_test_graph.list_edges() == [{'B', 'A'}])
        self.assertTrue(self.my_test_graph2.connected_components() == [{'A', 'B'},{'E', 'D'}] or self.my_test_graph2.list_edges() == [{'A', 'B'},{'D', 'E'}] or self.my_test_graph2.list_edges() == [{'B', 'A'},{'D', 'E'}] or self.my_test_graph2.list_edges() == [{'B', 'A'},{'E', 'D'}])

if __name__ == '__main__':
    unittest.main()