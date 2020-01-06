# Rating: ~ 1.4 / 10
# Link: https://open.kattis.com/problems/basketballoneonone

def main():
  l = input()
  a = 0
  b = 0
  for i, c in enumerate(l):
    if c == 'A':
      a += int(l[i+1])
    elif c == 'B':
      b += int(l[i+1])
  if a > b:
    print('A')
  else:
    print('B')

if __name__ == "__main__":
  main()
