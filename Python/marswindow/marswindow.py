# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/marswindow

def main():
  y, m = 2018, 3
  t = int(input())
  while True:
    if y == t:
      print('yes')
      return
    if y > t:
      print('no')
      return
    y += 2
    m += 2
    if m >= 12:
      y += 1
      m = m % 12

if __name__ == "__main__":
  main()
