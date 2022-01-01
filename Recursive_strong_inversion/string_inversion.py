import random
import string


class string_invertor:
    def __init__(self):
        pass
    def invert(self,_str):
        if _str == '':
            return ''
        else:
            return  self.invert(_str[1:]) + _str[0]
    def rev_invert(self,_str):
        if _str == '':
            return ''
        else:
            return  _str[-1] + self.rev_invert(_str[0:-1]) 

import unittest

class TestStringInversion(unittest.TestCase):
    def setUp(self):
        self.inverter = string_invertor()
        self.string_list = []
        for i in range(1000):
            # get random string of length 6 without repeating letters
            result_str = ''.join(random.sample(string.ascii_lowercase, 8))
            self.string_list.append(result_str)
    def test_inverter(self):
        for i in range(1000):
            self.assertEqual(self.inverter.invert(self.string_list[i]), self.inverter.rev_invert(self.string_list[i]))

if __name__ == '__main__':
    unittest.main()