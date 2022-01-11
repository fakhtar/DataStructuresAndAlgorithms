import random

class convert_binary:
    def __init__(self):
        pass
    def convert_binary(self,number: int) -> str:
        if number == 0:
            return number
        else:
            rem = number % 2
            return str(self.convert_binary(number//2)) + str(rem)


import unittest

class Testconvert_binary(unittest.TestCase):
    def setUp(self):
        self.convert_binary = convert_binary()
        self.int_list = []
        for i in range(1000):
            rand_int = random.randint(0, 10)
            self.int_list.append(rand_int)
    def test_converter(self):
        for i in range(1000):
            self.assertEqual('ob'+ self.convert_binary.convert_binary(self.int_list[i]), bin(self.int_list[i]))

if __name__ == '__main__':
    # convert_binary = convert_binary()
    # print(convert_binary.convert_binary(12))
    unittest.main()