# Rating: ~ 1.2 / 10
# Link: https://open.kattis.com/problems/timeloop
# Complexity: O(N) for N loops
# Memory: O(1)

def main():
  n = int(input());
  # trivial for loop
  for i in range(n):
    print(str(i+1), 'Abracadabra')

if __name__ == '__main__':
  main()
