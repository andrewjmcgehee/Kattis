# Rating: ~ 1.4 / 10
# Link: https://open.kattis.com/problems/avion

def main():
  out = []
  for i in range(1, 6):
    l = input()
    if l.find('FBI') != -1:
      out.append(str(i))
  if out:
    print(' '.join(out))
  else:
    print('HE GOT AWAY!')

if __name__ == "__main__":
  main()
