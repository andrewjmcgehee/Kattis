# Rating: ~ 4.5 / 10
# Link: https://open.kattis.com/problems/calculator
# Complexity: O(1)
# Memory: O(1)

def main():
  while True:
    try:
      # easy in python, if it were another language would probably have
      # to try to translate to post-fix and use a stack or something similar
      expr = input()
      ans = eval(expr)
      print("%.2f" % ans)
    except EOFError:
      break

if __name__ == '__main__':
  main()
