# Rating: ~ 1.4 / 10
# Link: https://open.kattis.com/problems/symmetricorder

def main():
  count = 1
  while True:
    x = int(input())
    if x == 0:
      break
    names = [input() for i in range(x)]
    left = names[::2]
    right = names[1::2]
    right = right[::-1]
    out = left + right
    print('SET {}'.format(count))
    for name in out:
      print(name)
    count += 1

if __name__ == "__main__":
  main()
