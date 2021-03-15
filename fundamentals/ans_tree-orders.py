# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.inOrderRecurser( 0)
                
    return self.result
  
  def inOrderRecurser( self, node_idx):
    if self.left[ node_idx] != -1:
      self.inOrderRecurser( self.left[ node_idx])
    self.result.append( self.key[ node_idx])
    if self.right[ node_idx] != -1:
      self.inOrderRecurser( self.right[ node_idx])
    return

  def preOrderRecurser( self, node_idx):
    self.result.append( self.key[ node_idx])
    if self.left[ node_idx] != -1:
      self.preOrderRecurser( self.left[ node_idx])
    if self.right[ node_idx] != -1:
      self.preOrderRecurser( self.right[ node_idx])
    return

  def postOrderRecurser( self, node_idx):
    if self.left[ node_idx] != -1:
      self.postOrderRecurser( self.left[ node_idx])
    if self.right[ node_idx] != -1:
      self.postOrderRecurser( self.right[ node_idx])
    self.result.append( self.key[ node_idx])
    return

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.preOrderRecurser( 0)        
    return self.result

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.postOrderRecurser( 0)
                
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
