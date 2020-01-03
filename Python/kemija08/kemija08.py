# Rating: ~ 1.4 / 10
# Link: https://open.kattis.com/problems/kemija08

def main():
  vowels = {'a', 'e', 'i', 'o', 'u'}
  line = input()
  out = []
  i = 0
  while i < len(line):
    out.append(line[i])
    if line[i] in vowels:
      i += 3
      continue
    i += 1
  print(''.join(out))

if __name__ == "__main__":
  main()
