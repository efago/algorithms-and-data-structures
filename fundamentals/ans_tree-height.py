# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
                # Replace this code with a faster implementation
                self.all_nodes= [ Node() for i in range( self.n)]
                root_idx= -1
                for i, parent in enumerate( self.parent):
                    if parent== -1:
                        root_idx= i
                    else:
                        self.all_nodes[ parent].children.append( i)
                return self.compute_node_height( self.all_nodes[ root_idx])

        def compute_node_height( self, node):
                children= node.children
                if len( children) == 0:
                    return 1
                height= 0
                for child in children:
                    height= max( self.compute_node_height( self.all_nodes[ child]) + 1, height)
                return height

class Node:
    def __init__( self):
        self.children= []

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
