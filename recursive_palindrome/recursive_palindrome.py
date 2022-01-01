import unittest


class palindrome_checker:
    def __init__(self):
        pass
    def check_palindrome(self, string_to_check):
        if len(string_to_check) == 0 or len(string_to_check) == 1:
            return True
        if string_to_check[0] == string_to_check[len(string_to_check) - 1]:
            return self.check_palindrome(string_to_check[1:-1])
        else:
            return False


        

class test_palindrome(unittest.TestCase):
    def setUp(self):
        self.checker = palindrome_checker()

    def test_palindrome(self):
        # self.assertEqual(self.inverter.invert(self.string_list[i]), self.inverter.rev_invert(self.string_list[i]))
        self.assertEqual(self.checker.check_palindrome("kayak"), True)
        self.assertEqual(self.checker.check_palindrome("abba"), True)
        self.assertEqual(self.checker.check_palindrome("mom"), True)
        self.assertEqual(self.checker.check_palindrome("k"), True)

if __name__ == '__main__':
    unittest.main()