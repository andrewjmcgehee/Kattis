# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/polymul1

from sys import stdin

def main():
  out = []
  lines = stdin.read().splitlines()
  cases = int(lines[0])
  for i in range(cases):
    deg_a, a, deg_b, b = lines[4*i+1:4*(i+1)+1]
    deg_a = int(deg_a)
    a = [int(x) for x in a.split()]
    deg_b = int(deg_b)
    b = [int(x) for x in b.split()]
    deg_c = deg_a + deg_b
    c = [0 for i in range(deg_c+1)]
    for i, u in enumerate(a):
      for j, v in enumerate(b):
        index = i + j
        c[index] += u*v
    out.append(str(deg_c))
    out.append(' '.join([str(x) for x in c]))
  print('\n'.join(out))



if __name__ == "__main__":
  main()
