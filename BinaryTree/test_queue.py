import unittest
import random
from queue import my_queue
from queue import naieveQueue

class test_queue(unittest.TestCase):
    def setUp(self):
        print('\n Run setup...')
        self.my_test_queue = my_queue()
        self.naieve_test_queue = naieveQueue()
    def tearDown(self):
        print('\n Run teardown...')
        pass
    def test_enqueue(self):
        print('enque is called with None to enque should raise an error...')
        self.assertRaises(ValueError,self.my_test_queue.enqueue,None)
        print('enque an item see if it returns the item that enqued ...')
        self.assertEqual(self.my_test_queue.enqueue(5),5)
    def test_dequeue(self):
        print('try to dequeue an item from empty queue and see if it raises an exceptoion ...')
        self.assertRaises(ValueError,self.my_test_queue.dequeue)
        # try to deque an item and see if that item is returned
        print('try to deque an item and see if that item is returned ...')
        self.my_test_queue.enqueue(5)
        self.assertEqual(self.my_test_queue.dequeue(),5)
    def test_front(self):
        # t
        print('try to get front from an empty queue should raise an error ...')
        self.assertRaises(ValueError,self.my_test_queue.front)
        # 
        self.my_test_queue.enqueue(5)
        self.my_test_queue.enqueue(7)
        print('try to get front from a queue...')
        self.assertEqual(self.my_test_queue.front(),5)
        pass
    def test_back(self):
        # 
        print('try to get back from an empty queue should raise an error...')
        self.assertRaises(ValueError,self.my_test_queue.back)
        # try to get back from a queue
        self.my_test_queue.enqueue(5)
        self.my_test_queue.enqueue(7)
        print('try to get back from a queue...')
        self.assertEqual(self.my_test_queue.back(),7)
    def test_vs_naieve(self):
        for i in range(0,100):
            my_int = random.randint(0, 50)
            self.my_test_queue.enqueue(my_int)
            self.naieve_test_queue.enqueue(my_int)
        for i in range(0,100):
            self.assertEqual(self.my_test_queue.back(),self.naieve_test_queue.back())
            self.assertEqual(self.my_test_queue.front(),self.naieve_test_queue.front())
            self.assertEqual(self.my_test_queue.dequeue(),self.naieve_test_queue.dequeue())
            self.assertEqual(self.my_test_queue.get_list(),self.naieve_test_queue.get_list())
            print('Regular')
            print(self.my_test_queue.get_list())
            print('Naieve')
            print(self.naieve_test_queue.get_list())

if __name__ == '__main__':
    unittest.main()