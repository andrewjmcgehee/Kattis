# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/longswaps
# Complexity: O(N log(N)) for union find with N elements
# Memory: O(N) for N characters in union find

# typical union method
def union(arr, a, b):
  arr[find(arr, a)] = find(arr, b)

# find method with path compression
def find(arr, a):
  if arr[a] == a:
    return a
  arr[a] = find(arr, arr[a])
  return arr[a]

def main():
  # inputs
  s, k = input().split()
  k = int(k)
  n = len(s)
  # build union find
  uf = [i for i in range(n)]
  for i in range(n):
    for j in range(i+k, n):
      # if the distance is k, then there is a "path" from s[i] to s[j]
      union(uf, j, i)
  # will store a character at it overall root using only valid swaps
  jumps = [[] for i in range(n)]
  for i in range(n):
    jumps[find(uf, i)].append(s[i])
  # sort the characters
  for i in range(n):
    jumps[i].sort()
  # find which character goes in which index using only valid swaps
  res = ''
  for i in range(n):
    root = uf[i]
    res += jumps[root][0]
    jumps[root].pop(0)
  # compare to what it should be if sorted
  target = ''.join(sorted(list(s)))
  if res == target:
    print("Yes")
  else:
    print("No")


if __name__ == "__main__":
  main()
