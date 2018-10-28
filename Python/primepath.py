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

is_prime = [True for i in range(10000)]

def sieve():
  for i in range(2, int(10000**(1/2.0))):
    if is_prime[i]:
      for j in range(i*i, 10000, i):
        is_prime[j] = False

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
  sieve()

  t = int(input())
  for _ in range(t):
    src, target = input().split()

    parent = dict()
    visited = set()
    q = Q()
    q.put(src)

    while not q.empty():
      current = q.get()
      if current in visited:
        continue
      if current == target:
        break
      visited.add(current)
      for neighbor in get_neighbors(current):
        if neighbor not in visited and not q.contains(neighbor):
          q.put(neighbor)
          parent[neighbor] = current

    path = []
    while target != src:
      path.append(target)
      target = parent[target]
    path.append(src)
    print(len(path)-1)

if __name__ == '__main__':
  main()
