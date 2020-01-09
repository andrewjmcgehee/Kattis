# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/dreamer

from itertools import permutations

def is_valid_year(date):
  year = int(date[4:])
  return year >= 2000

def is_leap(date):
  year = int(date[4:])
  if year % 4 != 0:
    return False
  if year % 4 == 0 and year % 100 != 0:
    return True
  if year % 100 == 0 and year % 400 != 0:
    return False
  if year % 400 == 0:
    return True
  return False

def is_valid_dm(date):
  days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  day = int(date[:2])
  month = int(date[2:4])
  if month < 1 or month > 12:
    return False
  month -= 1
  if is_leap(date):
    days[1] += 1
  if day <= 0 or day > days[month]:
    return False
  return True

def is_valid(date):
  return is_valid_dm(date) and is_valid_year(date)

def less_than(a, b):
  if b is None:
    return True
  ad = int(a[:2])
  bd = int(b[:2])
  am = int(a[2:4])
  bm = int(b[2:4])
  ay = int(a[4:])
  by = int(b[4:])
  if ay < by:
    return True
  elif ay == by:
    if am < bm:
      return True
    elif am == bm:
      if ad < bd:
        return True
      return False
    return False
  return False

def main():
  n = int(input())
  for _ in range(n):
    best = None
    valid = set()
    date = ''.join([x for x in input().split()])
    date = ''.join([x for x in sorted(list(date))])
    for d in permutations(date):
      d = ''.join(d)
      if is_valid(d):
        valid.add(d)
        if less_than(d, best):
          best = d
    if best is None:
      print(0)
      continue
    print(len(valid), best[:2], best[2:4], best[4:])

if __name__ == "__main__":
  main()
