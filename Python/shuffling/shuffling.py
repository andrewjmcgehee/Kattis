# Rating: ~ 2.9 / 10
# Link: https://open.kattis.com/problems/shuffling

def main():
  x, shuffle = input().split()
  x = int(x)

  seq = [i for i in range(x)]
  shuffled = seq[:]
  count = 0
  if shuffle == 'out':
    shuffled.pop(0)
  midpoint = len(shuffled) // 2
  while True:
    left = shuffled[:midpoint]
    right = shuffled[midpoint:]
    for i in range(len(left)):
      shuffled[2*i] = right[i]
      shuffled[2*i + 1] = left[i]
    if len(right) > len(left):
      shuffled[-1] = right[-1]
    if shuffle == 'in' and shuffled == seq:
      break
    elif shuffle == 'out':
      if [seq[0]] + shuffled == seq:
        break
    count += 1
  print(count+1)


if __name__ == "__main__":
  main()
