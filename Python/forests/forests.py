def main():
  p, t = map(int, input().split())
  opinions = [set() for i in range(p)]
  while True:
    try:
      op = [int(x) for x in input().split()]
    except EOFError:
      break
    person = op[0] - 1
    tree = op[1]
    opinions[person].add(tree)

  freq = dict()
  for i in range(p):
    opinions[i] = tuple(sorted(opinions[i]))
    if opinions[i] not in freq:
      freq[opinions[i]] = 0
    freq[opinions[i]] += 1
  print(len(freq.keys()))
if __name__ == '__main__':
  main()


