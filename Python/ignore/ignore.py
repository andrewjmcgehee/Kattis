# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/ignore

from sys import stdout, stdin

def convert(num):
  d, m = divmod(num, 7)
  if d > 0:
    return convert(d) + str(m)
  return str(m)

def replace(s):
  l = list(s)
  for i, dig in enumerate(l):
    if dig == '3':
      l[i] = '5'
    elif dig == '4':
      l[i] = '9'
    elif dig == '5':
      l[i] = '8'
  return ''.join(l)[::-1]

def main():
  for line in stdin:
    k = int(line)
    num = replace(convert(k))
    print(num)

if __name__ == "__main__":
  main()
