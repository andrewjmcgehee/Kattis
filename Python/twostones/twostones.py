# Rating: ~ 1.2 / 10
# Link: https://open.kattis.com/problems/twostones
# Complexity: O(1)
# Memory: O(1)

def main():
  i = int(input())
  # check even or odd
  if i % 2 == 0:
    stdout.write('Bob\n')
  else:
    stdout.write('Alice\n')

if __name__ == '__main__':
  main()
