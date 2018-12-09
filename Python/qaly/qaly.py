# Rating: ~ 1.2 / 10
# Link: https://open.kattis.com/problems/qaly
# Complexity: O(N) for N different queries
# Memory: O(1)

def main():
  n = int(input())
  # total
  qaly = 0
  for i in range(n):
    factor, time = map(float, input().split())
    # product of qaulity factor and time period of that quality
    qaly += factor*time
  print(qaly)

if __name__ == "__main__":
  main()
