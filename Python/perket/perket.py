# Rating: ~ 2.2 / 10
# Link: https://open.kattis.com/problems/perket

def main():
  n = int(input())
  ing = []
  for i in range(n):
    ing.append([int(x) for x in input().split()])

  best = float('inf')
  for i in range(1, 2**len(ing)):
    sour = 1
    bitter = 0
    for j in range(len(ing)):
      num = i >> j
      if num & 1:
        sour *= ing[j][0]
        bitter += ing[j][1]
    best = min(best, abs(sour - bitter))
  print(best)

if __name__ == "__main__":
  main()
