# Rating: ~ 3.8 / 10
# Link: https://open.kattis.com/problems/birthdayboy

days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# utility to get a numeric day [1, 365] for a given month day pair
def date_to_day(date):
  m, d = date
  return sum(days_in_month[:m]) + d

# get distance between two dates
def dist(b, a):
  a = date_to_day(a)
  b = date_to_day(b)
  if b < a:
    b += 365
  return b - a

def main():
  n = int(input())
  # filter uniques
  birthdays = set()
  for _ in range(n):
    _, date = input().split()
    m, d = map(int, date.split("-"))
    birthdays.add((m , d))
  # sort in chronological order
  birthdays = sorted(list(birthdays))

  # get distances between each pair (including wrap around)
  intervals = dict()
  for i in range(len(birthdays)):
    key = dist(birthdays[(i+1) % len(birthdays)], birthdays[i])
    if key not in intervals:
      intervals[key] = set()
    intervals[key].add(birthdays[(i+1) % len(birthdays)])

  best_interval = max(intervals.keys())
  # strictly after 10, 27
  m, d = 10, 28
  # indicates tie
  if len(intervals[best_interval]) > 1:
    # only 365 possible days so just cycle them
    while True:
      d += 1
      if d > days_in_month[m]:
        d = 1
        m += 1
        if m > 12:
          m = 1
      if (m, d) in intervals[best_interval]:
        break
  # unique solution
  else:
    m, d = intervals[best_interval].pop()
  # day before best birthday
  d -= 1
  if d < 1:
    m -= 1
    if m < 1:
      m = 12
    d = days_in_month[m]
  print('%02d-%02d' % (m, d))

if __name__ == "__main__":
  main()
