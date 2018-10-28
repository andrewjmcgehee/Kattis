def main():
  t = int(input())
  for _ in range(t):
    n = int(input())

    categories = dict()
    types = set()

    for i in range(n):
      piece, cat = input().split()
      if cat not in categories:
        categories[cat] = set()
        types.add(cat)
      categories[cat].add(piece)

    num = 1
    for i in types:
      num *= (len(categories[i])+1)
    num -= 1
    print(num)


if __name__ == '__main__':
  main()

