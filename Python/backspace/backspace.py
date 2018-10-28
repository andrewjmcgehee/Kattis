# Rating: ~ 2.8 / 10
# Link: https://open.kattis.com/problems/backspace
# Complexity: O(N) for N characters
# Memory: O(N) for N characters

def main():
  stack = []
  line = input()

  # use a stack
  for c in line:
    # don't append <'s
    if c != '<':
      stack.append(c)
    # when we see a < pop an item
    else:
      stack.pop()
  print(''.join(stack))

if __name__ == '__main__':
    main()
