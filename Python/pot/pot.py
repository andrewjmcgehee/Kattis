# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/pot
# Complexity: O(NK) for N strings and K characters in string representation of number
# Memory: O(1)

from sys import stdin

def main():
  ws = input()
  result = 0
  for line in stdin:
    line = line.strip()
    # raise num up to second to last char up to last char
    result += int(line[:-1])**int(line[-1])
  print(result))

if __name__ == '__main__':
  main()
