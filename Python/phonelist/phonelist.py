def main():
  t = int(input())
  for _ in range(t):
    n = int(input())
    nums = sorted([input() for i in range(n)], key=len)[::-1]
    prefixes = set()
    possible = True
    for num in nums:
      if num in prefixes:
        possible = False
        break
      for i in range(1, len(num)+1):
        prefixes.add(num[:i])
    if possible:
      print("YES")
    else:
      print("NO")

if __name__ == '__main__':
  main()

