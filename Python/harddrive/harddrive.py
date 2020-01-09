# Rating: ~ 3.0 / 10
# Link: https://open.kattis.com/problems/harddrive

def main():
  n, c, b = map(int, input().split())
  pos = [int(x) for x in input().split()]
  broken = [False for i in range(n)]
  bits = ['0' for i in range(n)]
  for p in pos:
    broken[p-1] = True

  i = n-1
  while i > 0:
    if not broken[i] and c > 1:
      bits[i] = '1'
      c -= 2
      i -=1
    i -= 1
  if c == 1:
    bits[0] = '1'
  print(''.join(bits))

if __name__ == "__main__":
  main()
