# Rating: ~ 3.2 / 10
# Link: https://open.kattis.com/problems/playfair
# Complexity: O(N) for N characters in text
# Memory: O(1) for cipher

# keep track of used letters
used = set()
alphabet = [
  'a', 'b', 'c', 'd', 'e',
  'f', 'g', 'h', 'i', 'j',
  'k', 'l', 'm', 'n', 'o',
  'p', 'r', 's', 't', 'u',
  'v', 'w', 'x', 'y', 'z'
]
cipher = [[0 for i in range(5)] for j in range(5)]

def main():
  # populate cipher
  key = input()
  # index in the key
  key_i = 0
  # index in the cipher
  i = 0
  while key_i < len(key):
    # row major
    row = i // 5
    col = i % 5
    char = key[key_i]
    # skip
    if char in used or char == ' ':
      key_i += 1
      continue
    # use
    used.add(char)
    cipher[row][col] = char
    i += 1
  # for the remaining cipher, use the alphabet
  for char in alphabet:
    row = i // 5
    col = i % 5
    if char in used:
      continue
    used.add(char)
    cipher[row][col] = char
    i += 1
  # put each char in message on stack
  stack = []
  message = input()
  for i in range(len(message)-1, -1, -1):
    # no spaces
    if message[i] != ' ':
      stack.append(message[i])

  encrypted = []
  while stack:
    # a+b is the two character digraph
    a = stack.pop()
    if stack:
      b = stack.pop()
    else:
      b = 'x'
    if a == b:
      stack.append(b)
      b = 'x'
    # find characters in cipher
    ax = -1
    ay = -1
    bx = -1
    by = -1
    for i in range(5):
      for j in range(5):
        if cipher[i][j] == a:
          ax = i
          ay = j
        if cipher[i][j] == b:
          bx = i
          by = j
    # same row
    if ax == bx:
      ay = (ay + 1) % 5
      by = (by + 1) % 5
      encrypted.append(cipher[ax][ay])
      encrypted.append(cipher[bx][by])
    # same col
    elif ay == by:
      ax = (ax + 1) % 5
      bx = (bx + 1) % 5
      encrypted.append(cipher[ax][ay])
      encrypted.append(cipher[bx][by])
    # neither
    else:
      encrypted.append(cipher[ax][by])
      encrypted.append(cipher[bx][ay])
  print(''.join(encrypted).upper())

if __name__ == '__main__':
  main()
