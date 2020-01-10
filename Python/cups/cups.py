# Rating: ~ 1.5 / 10
# Link: https://open.kattis.com/problems/cups

def main():
  n = int(input())
  cups = []
  for _ in range(n):
    a, b = input().split()
    if a[0] in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
      r = int(a) / 2
      color = b
    else:
      r = int(b)
      color = a
    cups.append((r, color))
  cups.sort()
  for c in cups:
    print(c[1])

if __name__ == "__main__":
  main()
