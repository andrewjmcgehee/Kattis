# Rating: ~ 1.8 / 10
# Link: https://open.kattis.com/problems/flexible
# Complexity: O(N^2) for N partitions
# Memory: O(N) for N partitions

def main():
  ins = [int(i) for i in input().split()]
  parts = [int(i) for i in input().split()]

  result = set()
  # add max size
  result.add(ins[0])

  # add all single partition sizes
  for i in parts:
    result.add(i)
    result.add(ins[0] - i)

  # add all pair-wise partition sizes
  for i in range(len(parts)):
    for j in range(i+1, len(parts)):
      result.add(parts[j] - parts[i])

  # cannot have a space of size 0
  if 0 in result:
    result.remove(0)

  result.sort()
  print(' '.join(str(x) for x in result))

if __name__ == '__main__':
    main()
