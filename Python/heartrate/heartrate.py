# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/heartrate
# Complexity: O(1)
# Memory: O(1)

def main():
  n = int(input())
  for i in range(n):
    a, b = map(float, input().split())
    # plus 1 beat and minus 1 beat
    print("%.4f %.4f %.4f" % ((a-1) * 60 / b, a * 60 / b, (a+1) * 60 / b))

if __name__ == "__main__":
  main()
