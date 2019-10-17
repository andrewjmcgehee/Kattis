# Rating: ~ 1.8 / 10
# Link: https://open.kattis.com/problems/princesspeach

def main():
  n, m = map(int, input().split())
  # keep track of distinct seen obstacles
  seen = set()
  for _ in range(m):
    obst = int(input())
    seen.add(obst)
  # print ones that aren't seen
  for i in range(n):
    if i not in seen:
      print(i)
  # length could be different since non distinct could show up
  print("Mario got %i of the dangerous obstacles." % len(seen))

if __name__ == "__main__":
  main()
