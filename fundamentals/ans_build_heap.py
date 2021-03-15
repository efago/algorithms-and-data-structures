# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
      n= int( np.log2( len( self._data)))
      for i in range( n, -1, -1):
          self.SiftDown( i)


  def SiftDown( self, i):
      size= len( self._data)
      left_idx= i * 2 + 1
      right_idx= ( i + 1) * 2
      min_idx= i
      if ( left_idx < size) and ( self._data[ left_idx] < self._data[ min_idx]):
          min_idx= left_idx
      if ( right_idx < size) and ( self._data[ right_idx] < self._data[ min_idx]):
          min_idx= right_idx
      if min_idx != i:
          self._swaps.append( [ i, min_idx])
          self._data[ i], self._data[ min_idx]= self._data[ min_idx], self._data[ i]
          self.SiftDown( min_idx)

  def Parent( self, i):
      return self._data[ int( ( i - 1) // 2)]
  def LeftChild( self, i):
      idx= i * 2 + 1
      child= 1e10
      if idx < len( self._data):
          child= self._data[ idx]
      return child
  def RightChild( self, i):
      idx= i * 2 + 1
      child= 1e10
      if idx < len( self._data):
          child= self._data[ idx]
      return child

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    import numpy as np
    heap_builder = HeapBuilder()
    heap_builder.Solve()
