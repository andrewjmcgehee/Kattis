# Rating: ~ 2.3 / 10
# Link: https://open.kattis.com/problems/primepath
# Complexity: O(V) for V vertices
# Memory: O(V) for V vertices

# custom q class for cheking if item in a queue
class Q:
  def __init__(self):
    self.q = []
    self.items = set()

  def get(self):
    if not self.empty():
      item = self.q[0]
      self.items.remove(item)
      del self.q[0]
      return item

  def put(self, item):
    self.q.append(item)
    self.items.add(item)

  def contains(self, x):
    return x in self.items

  def empty(self):
    return len(self.q) == 0

# primes array
is_prime = [True for i in range(10000)]

# sieve of eratosthenes for calculating primes 1 through n
def sieve():
  for i in range(2, int(10000**(1/2.0))):
    if is_prime[i]:
      for j in range(i*i, 10000, i):
        is_prime[j] = False

# helper function for bfs, eliminates bad neighbors
def get_neighbors(num):
  neighbors = []
  digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  for i in range(4):
    for digit in digits:
      new_num = num[:i] + digit + num[i+1:]
      if is_prime[int(new_num)] and new_num != num and int(new_num) >= 1000:
        neighbors.append(new_num)
  return neighbors


def main():
  # get primes
  sieve()

  t = int(input())
  for _ in range(t):
    src, target = input().split()

    # for rebuilding path, finding path length
    # could also be done in BFS by tracking BFS depth with sentinel value
    parent = dict()
    visited = set()
    q = Q()
    q.put(src)

    while not q.empty():
      current = q.get()
      # already been
      if current in visited:
        continue
      # found it
      if current == target:
        break
      # visit and add neighbors
      visited.add(current)
      for neighbor in get_neighbors(current):
        # dont re-add neighbors already in queue, highly connected graph
        if neighbor not in visited and not q.contains(neighbor):
          q.put(neighbor)
          parent[neighbor] = current
    # retrace path and get length
    path = []
    while target != src:
      path.append(target)
      target = parent[target]
    path.append(src)
    # path includes start node so subtract 1
    print(len(path)-1)

if __name__ == '__main__':
  main()
