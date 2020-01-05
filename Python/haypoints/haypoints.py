# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/haypoints

def main():
  n, m = map(int, input().split())
  value = dict()
  for i in range(n):
    name, val = input().split()
    value[name] = int(val)

  dot_count = 0
  vals = []
  while dot_count < m:
    total = 0
    line = ''
    while line != '.':
      line = input()
      for w in line.split():
        if w in value:
          total += value[w]
    print(total)
    dot_count += 1


if __name__ == "__main__":
  main()
