# Rating: ~ 2.4 / 10
# Link: https://open.kattis.com/problems/reachableroads
# Complexity: O(N log N) for union find
# Memory: O(N) for N cities

def union(arr, x, y):
  x_root = find(arr, x)
  y_root = find(arr, y)
  arr[y_root] = x_root

def find(arr, x):
  if arr[x] == x:
    return x
  arr[x] = find(arr, arr[x])
  return arr[x]

def main():
  n = int(input())
  for i in range(n):
    m = int(input())
    arr = [i for i in range(m)]
    r = int(input())
    for j in range(r):
      # union roads
      a, b = map(int, input().split())
      union(arr, a, b)

    # number of connected components
    comps = set()
    for j in range(m):
      # finding compresses path
      comps.add(find(arr, j))
    # for n cities, there are n-1 roads
    print(len(comps)-1)


if __name__ == "__main__":
  main()
