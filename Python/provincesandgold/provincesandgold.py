# Rating: ~ 1.4 / 10
# Link: https://open.kattis.com/problems/provincesandgold

def main():
  g, s, c = map(int, input().split())
  total = 3 * g + 2 * s + c
  vic = ''
  or_ = ''
  if total >= 8:
    vic = 'Province'
  elif total >= 5:
    vic = 'Duchy'
  elif total >= 2:
    vic = 'Estate'
  if vic != '':
    or_ = ' or '
  tre = 'Copper'
  if total >= 6:
    tre = 'Gold'
  elif total >= 3:
    tre = 'Silver'
  print(vic +  or_ + tre)

if __name__ == "__main__":
  main()
