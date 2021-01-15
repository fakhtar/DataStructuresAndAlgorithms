import unittest
import random
from collections import deque
from digraph import my_digraph

class test_graph(unittest.TestCase):
    def setUp(self):
        print('\n Run setup...')
    def tearDown(self):
        print('\n Run teardown...')
        pass
    def test_if_there_a_path_using_bellmanford_ex1(self):
        print('check if there is a path between two vertices using bellman ford...')
        self.my_test_graph = my_digraph({"A":{"B":(2,)},"B":{"C":(2,)},"C":{"A":(12,)}})
        print(self.my_test_graph)
        my_deq_test = deque()
        my_deq_test.append("C")
        my_deq_test.append("B")
        my_deq_test.append("A")        
        self.assertEqual(self.my_test_graph.bellman_ford("A","C"),my_deq_test)
    def test_if_there_a_path_using_bellmanford_ex2(self):
        print('check if there is a path between two vertices using bellman ford...')
        self.my_test_graph = my_digraph({"A":{"B":(2,)},"B":{"A":(2,)}})
        print(self.my_test_graph)
        my_deq_test = deque()
        my_deq_test.append("B")
        my_deq_test.append("A")        
        self.assertEqual(self.my_test_graph.bellman_ford("A","B"),my_deq_test)
    def test_if_there_a_path_using_bellmanford_ex3(self):
        print('check if there is a path between two vertices using bellman ford...')
        self.my_test_graph = my_digraph({"A":{"B":(2,)},"B":{"A":(2,)}})
        print(self.my_test_graph)
        my_deq_test = deque()
        my_deq_test.append("A")
        my_deq_test.append("B")        
        self.assertEqual(self.my_test_graph.bellman_ford("B","A"),my_deq_test)
if __name__ == '__main__':
    unittest.main()