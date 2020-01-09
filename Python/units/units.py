# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/units

def main():
  while True:
    n = int(input())
    if n == 0:
      break
    to_index = dict()
    to_name = dict()
    units = input().split()
    for i in range(n):
      to_index[units[i]] = i
      to_name[i] = units[i]
    adj = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
      adj[i][i] = 1
    for i in range(n-1):
      a, _, w, b = input().split()
      u = to_index[a]
      v = to_index[b]
      adj[u][v] = float(w)
      adj[v][u] = 1/float(w)
    # just needs to be run more than once
    for _ in range(2):
      for i in range(n):
        for j in range(n):
          if i == j:
            continue
          w1 = adj[i][j]
          if w1 != -1:
            for k in range(n):
              if k in {i,j}:
                continue
              w2 = adj[j][k]
              if w2 != -1:
                adj[i][k] = w1 * w2
                adj[k][i] = 1 / (w1*w2)
    largest = 0
    for i in range(n):
      smaller = False
      for j in range(n):
        if adj[i][j] < 1:
          smaller = True
          break
      if not smaller:
        largest = i
        break
    weights = []
    for i, w in enumerate(adj[largest]):
      weights.append((round(w), units[i]))
    weights.sort()
    out = []
    for w in weights:
      out.append(str(w[0]) + w[1])
    print(' = '.join(out))


if __name__ == "__main__":
  main()
