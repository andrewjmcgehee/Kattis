# Rating: ~
# Link:
# Complexity: O(
# Memory: O(

def main():
  while True:
    n = int(input())
    if n == -1:
      break

    adj = []
    for i in range(n):
      adj.append([int(x) for x in input().split()])

    # basically an edge list but with sets for quick lookup
    neighbors = dict()
    for i in range(n):
      neighbors[i] = set()
      for j in range(n):
        if adj[i][j] == 1:
          neighbors[i].add(j)

    weak = []
    # try every vertex
    for i in range(n):
      is_strong = False
      n1 = neighbors[i]
      # check all its neighbors
      for j in n1:
        # cannot re-include i
        n2 = neighbors[j] - {i}
        # check neighbors of neighbors
        for k in n2:
          # cannot re-include j
          n3 = neighbors[k] - {j}
          # if we find i, there is a triangle
          if i in n3:
            is_strong = True
            break
        if is_strong:
          break
      if not is_strong:
        weak.append(str(i))
    print(" ".join(weak))

if __name__ == '__main__':
  main()

