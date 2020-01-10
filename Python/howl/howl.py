# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/howl

def main():
  howl = ['A', 'W', 'H' 'O']
  h = len(input())
  while len(howl) <= h:
    howl.append('O')
  print(''.join(howl))

if __name__ == "__main__":
  main()
