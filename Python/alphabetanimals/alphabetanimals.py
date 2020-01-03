# alphabetanimals
# rating: 3.3

from sys import stdin
from collections import defaultdict

def main():
  lines = stdin.read().splitlines()
  start = lines[0][-1]
  x = int(lines[1])
  choices = [0 for i in range(26)]
  check = []
  for animal in lines[2:]:
    index = ord(animal[0]) - ord('a')
    choices[index] = True
    if animal[0] == start:
      check.append(animal)

  found = False
  if len(check) == 0:
    print('?')
    found = True
  elif len(check) == 1:
    if check[0][-1] == start:
      print(check[0] + '!')
      found = True
  else:
    for animal in check:
      letter = animal[-1]
      if not choices[ord(letter) - ord('a')]:
        print(animal + '!')
        found = True
        break
  if not found:
    print(check[0])

if __name__ == '__main__':
  main()
