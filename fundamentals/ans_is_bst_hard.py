#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if len( tree) == 0:
      return True
  if recurser( tree[ 0], tree, -1e10, 1e10) == False:
      return False
  return True

#min_val= -1e10, max_val= 1e10, node= tree[ 0]
def recurser( node, tree, min_val, max_val):
  if node[ 0] >= max_val or node[ 0] < min_val:
    return False
  if node[ 1] != -1:
    if tree[ node[ 1]][ 0] > node[ 0]:
      return False
    binaryness= recurser( tree[ node[ 1]], tree, min_val, node[ 0])
    if binaryness == False:
      return False
  if node[ 2] != -1:
    if tree[ node[ 2]][ 0] < node[ 0]:
      return False
    binaryness= recurser( tree[ node[ 2]], tree, node[ 0], max_val)
    if binaryness == False:
      return False
  return True

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
