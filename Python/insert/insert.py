# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/insert

memo = [[1 for _ in range(101)] for _ in range(101)]
for i in range(1, 101):
  for j in range(1, 101):
    memo[i][j] = memo[i-1][j] + memo[i][j-1]

class Node:
  def __init__(self, val):
    self.val = val
    self.children = 1
    self.l = None
    self.r = None

def insert(root, val):
  if root is None:
    root = Node(val)
    return root
  if val < root.val:
    root.l = insert(root.l, val)
  else:
    root.r = insert(root.r, val)
  root.children += 1
  return root

def count(root):
  if root is None:
    return 1
  total = 1
  if root.r is not None and root.l is not None:
    total = memo[root.l.children][root.r.children]
  total *= count(root.l)
  total *= count(root.r)
  return total

def main():
  while True:
    root = None
    try:
      n = int(input())
      vals = [int(x) for x in input().split()]
    except:
      break
    for v in vals:
      root = insert(root, v)
    print(count(root))

if __name__ == "__main__":
  main()
