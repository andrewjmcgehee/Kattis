# Rating: ~ 1.4 / 10
# Link: https://open.kattis.com/problems/zanzibar

def main():
  x = int(input())
  for i in range(x):
    t = [int(x) for x in input().split()]
    t = t[:-1]
    total = 0
    for j in range(1, len(t)):
      if t[j] > 2 * t[j-1]:
        total += t[j] - 2*t[j-1]
    print(total)

if __name__ == "__main__":
  main()
