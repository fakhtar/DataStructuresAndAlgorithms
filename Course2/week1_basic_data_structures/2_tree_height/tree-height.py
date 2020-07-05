# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

# class TreeHeight:
#         def read(self):
#                 self.n = int(sys.stdin.readline())
#                 self.parent = list(map(int, sys.stdin.readline().split()))

#         def compute_height(self):
#                 # Replace this code with a faster implementation
#                 maxHeight = 0
#                 for vertex in range(self.n):
#                         height = 0
#                         i = vertex
#                         while i != -1:
#                                 height += 1
#                                 i = self.parent[i]
#                         maxHeight = max(maxHeight, height);
                # return maxHeight

# def main():
#   tree = TreeHeight()
#   tree.read()
#   print(tree.compute_height())
def height(p_key,tree):
        if p_key not in tree:
                return 1
        children = tree[p_key]
        depth = []
        for child in children:
                depth.append(height(child,tree))
        return 1 + max(depth)


def calc_height(num_nodes, nodes):
        tree = {}
        for i in range(0,num_nodes):
                node = nodes[i]
                if node in tree:
                        tree[node].append(i)
                else:
                        tree[node] = [i]
        parent_key = tree[-1][0]
        return height(parent_key,tree)


# for item in [(5,'4 -1 4 1 1',3),(5,'-1 0 4 0 3',4)]:
#         nodes = list(map(int, item[1].split()))
#         if calc_height(item[0],nodes) != item[2]:
#                 print('Error')

def main():
        num_nodes = int(sys.stdin.readline())
        nodes = list(map(int, sys.stdin.readline().split()))
        print(calc_height(num_nodes,nodes))




threading.Thread(target=main).start()
