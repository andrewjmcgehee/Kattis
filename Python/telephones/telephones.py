# Rating: ~ 2.7 / 10
# Link: https://open.kattis.com/problems/telephones

def main():
  while True:
    n, m = map(int, input().split())
    if n == m == 0:
      break
    calls = []
    for i in range(n):
      _, _, s, d = map(int, input().split())
      calls.append((s, s+d))
    for i in range(m):
      s, d = map(int, input().split())
      e = s+d
      total = 0
      for a, b in calls:
        if (a <= s and b > s) or (a < e and b > e) or (a >= s and b <= e):
          total += 1
      print(total)


if __name__ == "__main__":
  main()
