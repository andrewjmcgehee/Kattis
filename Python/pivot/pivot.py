# Rating: ~ 2.8 / 10
# Link: https://open.kattis.com/problems/pivot
# Complexity: O(N) for an array of size N
# Memory: O(N) for sets containing pivot candidates

def main():
  n = int(input())
  arr = [int(x) for x in input().split()]

  # a set containing all values which satisfy the first criteria
  # they are greater than or equal to all values in the left sub
  # array
  greater_than_left = set()
  # first value in array always passes this condition
  greater_than_left.add(arr[0])

  # set containing values which satisfy second criteria where they
  # are less than or equal to all values in right sub array
  less_than_right = set()
  # last value in array always passes this condition
  less_than_right.add(arr[-1])

  # keep track of current max seen as we scan the array left to right
  current_max = arr[0]
  for i in range(1, n):
    # if this value is greater/equal it qualifies
    if arr[i] >= current_max:
      greater_than_left.add(arr[i])
    # update max
    current_max = max(arr[i], current_max)

  # keep track of current min as we scan array right to left
  current_min = arr[-1]
  for i in range(len(arr)-2, -1, -1):
    # if it is less/equal it qualifies
    if arr[i] <= current_min:
      less_than_right.add(arr[i])
    current_min = min(arr[i], current_min)

  # intersection of sets of criterion holds the pivots
  pivots = greater_than_left & less_than_right
  print(len(pivots))


if __name__ == "__main__":
  main()
