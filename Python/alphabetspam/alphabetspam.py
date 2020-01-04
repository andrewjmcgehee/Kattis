# Rating: ~ 1.4 / 10
# Link: https://open.kattis.com/problems/alphabetspam

def is_lower(c):
  return ord(c) >= 65+32 and ord(c) < 65+32+26

def is_upper(c):
  return ord(c) >= 65 and ord(c) < 65+26

def main():
  l = input()
  total = len(l)
  lower = 0
  upper = 0
  symbol = 0
  white = 0
  for c in l:
    if c == '_':
      white += 1
    elif is_lower(c):
      lower += 1
    elif is_upper(c):
      upper += 1
    else:
      symbol += 1
  print(white / total)
  print(lower / total)
  print(upper / total)
  print(symbol / total)

if __name__ == "__main__":
  main()
