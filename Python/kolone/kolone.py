def main():
  ws = input()
  n = list(input())[::-1]
  m = list(input())
  t = int(input())

  if t >= len(n) + len(m):
    print(''.join(m + n))
  else:
    indices = dict()
    i = 0
    for char in n:
      indices[char] = i
      i += 1
    for char in m:
      indices[char] = i
      i += 1


    new = ['0' for i in range(len(n) + len(m))]
    i = t
    index = len(n) - 1
    while i and (index + 1):
      char = n[index]
      indices[char] = min(indices[char] + i, index + len(m))
      i -= 1
      index -= 1

    i = t
    index = 0
    while i and index < len(m):
      char = m[index]
      indices[char] = max(indices[char] - i, index)
      i -= 1
      index += 1

    for char in indices:
      new[indices[char]] = char
    print(''.join(new))

if __name__ == '__main__':
  main()

