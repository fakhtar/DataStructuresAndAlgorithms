import random

class fib:
    def __init__(self):
        self.memo = {}
    def memo_fib(self,n: int) -> int:
        if n == 0 or n == 1:
            return n
        else:
            if n-1 not in self.memo:
                fib1 = self.memo_fib(n -1)
            else:
                fib1 = self.memo[n-1]
            if n-2 not in self.memo:
                fib2 = self.memo_fib(n -2)
            else:
                fib2 = self.memo[n-2]
            return fib1 + fib2
    def regular_fib(self,n: int) -> int:
        if n == 0 or n == 1:
            return n
        else:
            return self.memo_fib(n -1) + self.memo_fib(n -2)



import unittest

class testfib(unittest.TestCase):
    def setUp(self):
        self.fib = fib()
        self.int_list = []
        for i in range(1000):
            rand_int = random.randint(0, 20)
            self.int_list.append(rand_int)
    def test_fib(self):
        for i in range(1000):
            self.assertEqual(self.fib.memo_fib(self.int_list[i]), self.fib.regular_fib(self.int_list[i]))

if __name__ == '__main__':
    # convert_binary = convert_binary()
    # print(convert_binary.convert_binary(12))
    unittest.main()