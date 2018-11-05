# Rating: ~ 1.9 / 10
# Link: https://open.kattis.com/problems/t9spelling
# Complexity: O(N) for N characters
# Memory: O(N) for N characters

def main():
  # nasty map that maps each character to its respective keypad sequence
  table = {
    'a': '2',
    'b': '22',
    'c': '222',
    'd': '3',
    'e': '33',
    'f': '333',
    'g': '4',
    'h': '44',
    'i': '444',
    'j': '5',
    'k': '55',
    'l': '555',
    'm': '6',
    'n': '66',
    'o': '666',
    'p': '7',
    'q': '77',
    'r': '777',
    's': '7777',
    't': '8',
    'u': '88',
    'v': '888',
    'w': '9',
    'x': '99',
    'y': '999',
    'z': '9999',
    ' ': '0'
  }

  t = int(input())
  for test in range(t):
    ans = []
    text = input()
    # always safe to add first char
    ans.append(table[text[0]])
    prev = ans[0]
    for i in range(1, len(text)):
      char = table[text[i]]
      # check previous character to know if space needed
      if char[0] == prev[0]:
        ans.append(' ')
      ans.append(char)
      prev = char
    # handle output
    print("Case #%i: %s" % (test+1, ''.join(ans)))

if __name__ == '__main__':
  main()


