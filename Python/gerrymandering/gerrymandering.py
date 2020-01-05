# Rating: ~ 1.4 / 10
# Link: https://open.kattis.com/problems/gerrymandering

from collections import defaultdict

def main():
  n, m = map(int, input().split())
  a_dist = defaultdict(int)
  b_dist = defaultdict(int)
  total = 0
  for i in range(n):
    d, a, b = map(int, input().split())
    a_dist[d] += a
    b_dist[d] += b
    total += a + b
  a_waste = 0
  b_waste = 0
  for k in sorted(a_dist.keys()):
    maj = (a_dist[k] + b_dist[k]) // 2 + 1
    if a_dist[k] > b_dist[k]:
      a_waste += a_dist[k] - maj
      b_waste += b_dist[k]
      print('A {} {}'.format(a_dist[k] - maj, b_dist[k]))
    else:
      a_waste += a_dist[k]
      b_waste += b_dist[k] - maj
      print('B {} {}'.format(a_dist[k], b_dist[k] - maj))
  print(abs(a_waste-b_waste)/total)



if __name__ == "__main__":
  main()
