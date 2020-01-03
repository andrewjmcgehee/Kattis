# Rating: ~ 1.4 / 10
# Link: https://open.kattis.com/problems/licensetolaunch

def main():
  _ = input()
  x = [int(x) for x in input().split()]
  print(x.index(min(x)))

if __name__ == "__main__":
  main()
