import unittest
import random
import json
from trie import my_trie
from trie import naieve_trie

class test_queue(unittest.TestCase):
    def setUp(self):
        print('\n Run setup...')
        self.my_test_trie = my_trie()
        self.naieve_test_trie = naieve_trie()
    def tearDown(self):
        print('\n Run teardown...')
        pass
    def test_insert_word_only_accept_string(self):
        # arrange
        # act
        self.assertRaises(ValueError,self.my_test_trie.insert_word,1)
        # assert
    def test_insert_word_return_type_none(self):
        # arrange
        # act
        self.assertIsNone(self.my_test_trie.insert_word("test"))
        # assert
    def test_insert_word_twice_return_type_none(self):
        # arrange
        # act
        # assert
        self.assertIsNone(self.my_test_trie.insert_word("test"))
        self.assertIsNone(self.my_test_trie.insert_word("test"))
    def test_insert_word_insert_blank_string(self):
        # arrange
        # act
        # assert
        self.assertRaises(ValueError,self.my_test_trie.insert_word,'')
    def test_is_word_return_type_bool(self):
        # arrange
        # act
        test_bool = self.my_test_trie.is_word("test")
        # assert
        self.assertEqual(type(test_bool),bool)
    def test_is_word_only_accept_string(self):
        # arrange
        # act
        self.assertRaises(ValueError,self.my_test_trie.is_word,1)
        # assert
    def test_is_word_insert_blank_string(self):
        # arrange
        # act
        # assert
        self.assertRaises(ValueError,self.my_test_trie.is_word,'')
    def test_is_word_valid_word_returns_true(self):
        # arrange
        # act
        self.my_test_trie.insert_word("car")
        self.my_test_trie.insert_word("cart")
        self.my_test_trie.insert_word("cartoon")
        # assert
        self.assertEqual(self.my_test_trie.is_word("cartoon"),True)
    def test_is_word_valid_word_returns_false(self):
        # arrange
        # act
        self.my_test_trie.insert_word("car")
        self.my_test_trie.insert_word("cart")
        self.my_test_trie.insert_word("cartoon")
        # assert
        self.assertEqual(self.my_test_trie.is_word("cartoo"),False)
    def test_is_word_valid_word_returns_false_for_word_larger_than_all_others(self):
        # arrange
        # act
        self.my_test_trie.insert_word("car")
        self.my_test_trie.insert_word("cart")
        self.my_test_trie.insert_word("cartoon")
        # assert
        self.assertEqual(self.my_test_trie.is_word("cartoooooooooooooooo"),False)
    def test_is_word_valid_word_returns_false_for_medium_word(self):
        # arrange
        # act
        self.my_test_trie.insert_word("car")
        self.my_test_trie.insert_word("cart")
        self.my_test_trie.insert_word("cartoon")
        # assert
        self.assertEqual(self.my_test_trie.is_word("ca"),False)
    def test_efficeint_vs_naieve(self):
        choices = []
        with open('words_dictionary.json') as f:
            data = json.load(f)
        for i in range (0,5000):
            choice = random.choice(list(data.keys()))
            self.my_test_trie.insert_word(choice)
            self.naieve_test_trie.insert_word(choice)
            choices.append(choice)
        print('break--------------------------------------------------------------break')
        print(choices)
        for choice in choices:
            print(choice)
            self.assertEqual(self.my_test_trie.is_word(choice),self.naieve_test_trie.is_word(choice))

if __name__ == '__main__':
    unittest.main()