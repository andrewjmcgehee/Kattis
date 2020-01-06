# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/communication

def main():
  n = int(input())
  byte_arr = [int(x) for x in input().split()]
  decoded = []
  for b in byte_arr:
    for i in range(256):
      if i ^ (i << 1) % 256 == b:
        decoded.append(str(i))
        break
  print(' '.join(decoded))


if __name__ == "__main__":
  main()
