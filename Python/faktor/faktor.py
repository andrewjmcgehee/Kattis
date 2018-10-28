# Rating: ~ 1.2 / 10
# Link: https://open.kattis.com/problems/faktor
# Complexity: O(1)
# Memory: O(1)

def main():
  # simple ad hoc
  ins = [int(x) for x in input().split()]
  print(ins[0] * (ins[1] - 1) + 1)

if __name__ == '__main__':
    main()
