# Rating: ~ 3.8 / 10
# Link: https://open.kattis.com/problems/thanosthehero

def main():
  n = int(input())
  worlds = [int(x) for x in input().split()]
  total = 0
  for i in range(n-2, -1, -1):
    val = min(worlds[i], worlds[i+1]-1)
    if worlds[i] > val:
      total += worlds[i] - val
      worlds[i] = val
  if worlds[0] < 0:
    print(1)
  else:
    print(total)

if __name__ == "__main__":
  main()
