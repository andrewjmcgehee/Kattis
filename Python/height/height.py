# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/height

def main():
  n = int(input())
  for _ in range(n):
    c, *a = map(int, input().split())
    total = 0
    for i in range(len(a)):
      for j in range(i):
        if a[j] > a[i]:
          total += 1
    print(c, total)

if __name__ == "__main__":
  main()
