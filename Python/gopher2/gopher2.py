# Rating: ~ 4.9 / 10
# Link: https://open.kattis.com/problems/gopher2
# Complexity: O(VE) i am assuming as this is very similar to ford-fulkerson
# Memory: O(NK) for N gophers and K holes

# can be modeled as bipartite graph for gophers and holes
class Bipartite:
  def __init__(self, a, b):
    # num gophers
    self.a = a
    # num holes
    self.b = b
    # edge list
    self.edges = [[] for i in range(a)]
    self.visited = [False for i in range(b)]
    # stores the matching where match[u] = v indicates U matches to V
    self.matches = [0 for i in range(b)]

  # helper for adding edges to graph
  def add_edge(self, i, j):
    self.edges[i].append(j)

  # bipartite matching, very similar to dfs
  def bpm(self, u):
    # if we havent visited an edge visit it
    for i, v in enumerate(self.edges[u]):
      if not self.visited[v]:
        self.visited[v] = True
        # very similar to dfs but guaranteed match,
        # slight modification to dfs behavior where if the edge has
        # already been match we can recurse on the node it matches to
        if self.matches[v] == -1 or self.bpm(self.matches[v]):
          self.matches[v] = u
          return True
    return False

  # finds the max bipartite matching
  def max_bpm(self):
    res = 0
    # initially no matches
    self.matches = [-1 for i in range(self.b)]
    for i in range(self.a):
      # initially no visited
      self.visited = [False for x in range(self.b)]
      # when a match is found, increment the result
      if self.bpm(i):
        res += 1
    return res

def main():
  while True:
    try:
      # inputs
      n, m , s, v = map(int, input().split())
      # maximum distance = r^2 = x^2 + y^2
      MAX_DIST = (s*v)**2

      # get coords
      gophers = []
      holes = []
      for i in range(n):
        g = tuple(map(float, input().split()))
        gophers.append(g)
      for i in range(m):
        h = tuple(map(float, input().split()))
        holes.append(h)

      # build graph
      bpg = Bipartite(n, m)
      for i, g in enumerate(gophers):
        for j, h in enumerate(holes):
          # edge only exists if the distance is less than or equal to
          # the max distance possible in the time limit
          dist = (g[0] - h[0])**2 + (g[1] - h[1])**2
          if dist <= MAX_DIST:
            bpg.add_edge(i, j)
      # vulnerable gophers will be the ones left AFTER max flow calculated
      print(n - bpg.max_bpm())
    except:
      break

if __name__ == '__main__':
  main()
