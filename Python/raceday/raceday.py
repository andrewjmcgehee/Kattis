# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/raceday
# Complexity: O(N log(N)) for N runners for sorting
# Memory: O(N) for N runners

# helper function to figure out ranks
def rank(arr, names):
  # current rank
  place = 0
  prev_time = 0
  # will keep track of how many have the same rank due to same time
  offset = 1
  res = arr[:]
  for i in range(len(arr)):
    m, s, num = arr[i]
    # time in seconds for comparison
    time = 60*m + s
    # new rank encountered
    if time > prev_time:
      # if multiple with same rank have been seen, rank increases by that number
      place += offset
      res[i] = (names[num][0], names[num][1], place, m, s)
      prev_time = time
      # reset offset
      offset = 1
    # same time, because arr is already sorted
    else:
      res[i] = (names[num][0], names[num][1], place, m, s)
      # grow offset
      offset += 1
  return res

def main():
  while True:
    n = int(input())
    if n == 0:
      break

    # for ease of translation between name and number
    nums_to_names = dict()
    runners = []
    for i in range(n):
      first, last, num = input().split()
      runners.append((last, first, num))
      nums_to_names[num] = (last, first)
    # sorted alphabetically by last name and then first
    runners.sort()

    # each split
    s1 = []
    s2 = []
    f = []
    for i in range(3*n):
      num, split, time = input().split()
      # get minutes and seconds for sorting
      m, s = map(int, time.split(':'))
      if split == 'S1':
        s1.append((m, s, num))
      elif split == 'S2':
        s2.append((m, s, num))
      else:
        f.append((m, s, num))
    # sort by times
    s1.sort()
    s2.sort()
    f.sort()
    # find ranks
    s1 = rank(s1, nums_to_names)
    s2 = rank(s2, nums_to_names)
    f = rank(f, nums_to_names)
    # sort by names again
    s1.sort()
    s2.sort()
    f.sort()
    # will hold table
    res = []
    # easiest just to copy and past first row
    res.append("NAME                       BIB    SPLIT1      RANK    SPLIT2      RANK    FINISH      RANK")
    for i in range(n):
      # since final ranks and runners sorted by names, we can just use one index
      last, first, num = runners[i]
      name = last + ", " + first
      # get rank and time info
      s1_rank, s1_m, s1_s = s1[i][2:]
      s2_rank, s2_m, s2_s = s2[i][2:]
      f_rank, f_m, f_s = f[i][2:]
      # convert times to valid 0 padded digits
      s1_time = "{:02d}:{:02d}".format(s1_m, s1_s)
      s2_time = "{:02d}:{:02d}".format(s2_m, s2_s)
      f_time = "{:02d}:{:02d}".format(f_m, f_s)
      # format string
      line = "{:20s}{:>10s}{:>10s}{:>10d}{:>10s}{:>10d}{:>10s}{:>10d}".format(
          name,
          num,
          s1_time,
          s1_rank,
          s2_time,
          s2_rank,
          f_time,
          f_rank
      )
      res.append(line)
    # table joined by new lines and new line after each test case
    print('\n'.join(res))
    print()


if __name__ == "__main__":
  main()
