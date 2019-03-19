# Rating: ~ 3.0 / 10
# Link: https://open.kattis.com/problems/bitbybit
# Complexity: O(N) for N operations
# Memory: O(1) 32 "bits"

def main():
  # handle file input
  while True:
    x = int(input())
    if x == 0:
      break

    # -1 to represent question marks
    num = [-1 for j in range(32)]
    for i in range(x):
      instr = input()
      # AND
      if instr.startswith('A'):
        a, b = map(int, instr.split()[1:])
        # both are 1 forces to 1
        if num[-1-a] == 1 and num[-1-b] == 1:
          num[-1-a] = num[-1-a] & num[-1-b]
        # either are 0 forces to 0
        elif num[-1-a] == 0 or num[-1-b] == 0:
          num[-1-a] = 0
        # unknown
        else:
          num[-1-a] = -1
      # OR
      elif instr.startswith('O'):
        a, b = map(int, instr.split()[1:])
        # either are 1 forces to 1
        if num[-1-a] == 1 or num[-1-b] == 1:
          num[-1-a] = 1
        # both are 0 forces to 0
        elif num[-1-a] == 0 and num[-1-b] == 0:
          num[-1-a] = 0
        # unknown
        else:
          num[-1-a] = -1
      # set to 0
      elif instr.startswith('C'):
        a = int(instr.split()[-1])
        num[-1-a] = 0
      # set to 1
      else:
        a = int(instr.split()[-1])
        num[-1-a] = 1
    # format and print
    out = ''
    for i in range(32):
      if num[i] == -1:
        out += '?'
      else:
        out += str(num[i])
    print(out)

if __name__ == "__main__":
  main()
