# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/datum

def main():
  days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  days_of_week = [
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday'
  ]
  d, m = map(int, input().split())
  day = sum(days_in_month[:m-1]) + d - 1
  print(days_of_week[day%7])

if __name__ == "__main__":
  main()
