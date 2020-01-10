# Rating: ~ 1.5 / 10
# Link: https://open.kattis.com/problems/modulo

def main():
  vals = set()
  for _ in range(10):
    x = int(input()) % 42
    vals.add(x)
  print(len(vals))

if __name__ == "__main__":
  main()
