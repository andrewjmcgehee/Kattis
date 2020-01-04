# Rating: ~ 2.3 / 10
# Link: https://open.kattis.com/problems/peasoup

def main():
  n = int(input())
  for i in range(n):
    k = int(input())
    name = input()
    items = set()
    for j in range(k):
      items.add(input())
    if 'pea soup' in items and 'pancakes' in items:
      print(name)
      break
  else:
    print('Anywhere is fine I guess')

if __name__ == "__main__":
  main()
