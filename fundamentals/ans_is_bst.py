#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if len( tree) < 2:
    return True
  order_list= recurser( 0, tree, [])
  val= -1e10
  binaryness= True
  for i, key in enumerate( order_list):
    if key < val:
      binaryness= False
      break
    val= key
  print( order_list)
  return binaryness


def recurser( node, tree, order_list):
  if tree[ node][ 1] != -1:
    recurser( tree[ node][ 1], tree, order_list)
  order_list.append( tree[ node][ 0])
  if tree[ node][ 2] != -1:
    recurser( tree[ node][ 2], tree, order_list)

  return order_list

  def inOrderRecurser( self, node_idx):
    if self.left[ node_idx] != -1:
      self.inOrderRecurser( self.left[ node_idx])
    self.result.append( self.key[ node_idx])
    if self.right[ node_idx] != -1:
      self.inOrderRecurser( self.right[ node_idx])
    return

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
