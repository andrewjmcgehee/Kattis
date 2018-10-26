# This is not a solution to a kattis problem. This is a python implementation of
# a fenwick tree

# returns sum of arr[0..index] inclusive
def get_sum(fenwick, index):
  total = 0

  # index in fenwick[] is 1 more than the index in arr[]
  i = index+1

  # traverse tree
  while i > 0:
    total += fenwick[i]
    # get parent by removing least significant bit
    i -= i & (-i)
  return total

# updates a node in fenwick tree at given index
# the given value val is added to fenwick[i] and
# all of its ancestors in tree
def update(fenwick, index, value):

  # index in fenwick[] is 1 more than the index in arr[]
  i = index+1
  n = len(fenwick)-1

  # traverse all ancestors and add 'val'
  while i <= n:
    # add val to current node of tree
    fenwick[i] += value

    # updates children
    i += i & (-i)

# builds fenwick tree
def construct(arr):
  n = len(arr)
  fenwick = [0] * (n+1)

  for i in range(n):
    update(fenwick, i, arr[i])
  return fenwick

