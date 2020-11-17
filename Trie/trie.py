import json
import random


class _trie_node:
    def __init__(self, character: str):
        self.character = character
        self.children = {}
        self.is_word =  False

class my_trie:
    def __init__(self):
        self.root = _trie_node(None)
        self.curr_node =  self.root
    def insert_word(self,word: str) -> None:
        if (type(word) is not str or word == ''):
            raise ValueError('This trie only supports string arguments.')
        word_len = len(word)
        i = 0
        for character in word:
            # if current character is in the node, then proceed to next character
            if character in self.curr_node.children:
                self.curr_node = self.curr_node.children[character]
                i += 1
                continue
            else:
                new_node = _trie_node(character)
                self.curr_node.children[character] = new_node
                self.curr_node = new_node
                i += 1
            # if the word has ended, then the current node represents a word
        if word_len == i:
            self.curr_node.is_word = True
        self.curr_node = self.root
        return None
    def is_word(self,word: str) -> bool:
        if (type(word) is not str  or word == ''):
            raise ValueError('This trie only supports string arguments.')
        i = 0
        for character in word:
            # if current character is in the node, then proceed to next character
            if character in self.curr_node.children:
                self.curr_node = self.curr_node.children[character]
                i += 1
                continue
            else:
                self.curr_node = self.root 
                return False
        temp_bool = self.curr_node.is_word
        self.curr_node = self.root       
        return temp_bool

class naieve_trie:
    def __init__(self):
        self.my_list = []
    def insert_word(self,word: str) -> None:
        if (type(word) is not str or word == ''):
            raise ValueError('This trie only supports string arguments.')
        self.my_list.append(word)
        return None
    def is_word(self,word: str) -> bool:
        if (type(word) is not str  or word == ''):
            raise ValueError('This trie only supports string arguments.')
        return word in self.my_list

if __name__ == '__main__':
    test_trie = my_trie()
    # test_trie.insert_word('car')
    # test_trie.insert_word('cart')
    # test_trie.insert_word('cart')
    # test_trie.insert_word('bi')
    # test_trie.is_word('careee')
    # test_trie.is_word('ca')
    # test_trie.is_word('bi')
    test_naieve_trie = naieve_trie()
    test_fail = ['mateship', 'noyous', 'harassingly', 'thurniaceae', 'oximeter', 'sawhorses', 'absolving', 'interregnal', 'symbolistic', 'soloistic', 'bowne', 'aftergame', 'ballades', 'dehydroffrozen', 'klephts', 'unforgetfulness', 'callose', 'contractable', 'javanese', 'poachiest', 'dahs', 'overstrained', 'hadj', 'digitalin', 'surgers', 'undeserver', 'dertra', 'quickthorn', 'magicians', 'polymixiidae', 'megalopidae', 'astutious', 'lysogenize', 'marok', 'crenature', 'abridger', 'iberite', 'listers', 'ophisaurus', 'residual', 'inflexibly', 'sapharensian', 'naology', 'abridge', 'quercinic', 'gonidia', 'adherescent', 'hoarhead', 'daimios', 'nonlethal']
    for choice in test_fail:
        if choice == "abridge":
            test_trie.insert_word(choice)
        test_trie.insert_word(choice)
        test_naieve_trie.insert_word(choice)
        # print(choice)
    for choice in test_fail:
        print('------------------------------------------------------')
        print(choice)
        print(test_trie.is_word(choice))
        print(test_trie.is_word(choice))
        if (test_trie.is_word(choice) != test_naieve_trie.is_word(choice)):
            test_trie.is_word(choice)

    # test_naieve_trie = naieve_trie()
    # test_naieve_trie.insert_word('car')
    # test_naieve_trie.insert_word('cart')
    # test_naieve_trie.insert_word('cart')
    # test_naieve_trie.is_word('careee')
    # test_naieve_trie.is_word('ca')
    # test_naieve_trie.is_word('car')
    # with open('words_dictionary_short.json') as f:
    #     data = json.load(f)
    # print(data)
    # print(random.choice(list(data.keys())))
    