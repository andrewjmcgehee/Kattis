# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/averagespeed
# Complexity: O(N) for N time intervals
# Memory: O(N) for N intervals

def main():
  # get all inputs at once
  ins = []
  while True:
    try:
      line = input()
      ins.append(line.split())
    except EOFError:
      break

  # initially 0 distance and 0 speed
  dists = [0]
  speeds = [0]

  for i in range(len(ins)):
    end = [int(x) for x in ins[i][0].split(':')]
    start = [int(x) for x in ins[i-1][0].split(':')]
    # scaling factor for speed
    # each hour adds 1, each minute 1 / 60, each second 1 / 3600
    factor = (end[0] - start[0]) + (end[1] - start[1]) / 60 + (end[2] - start[2]) / 3600

    # add the new distance at the previous speed
    dists.append(factor * speeds[-1])
    # if updating the speed
    if len(ins[i]) > 1:
      speeds.append(int(ins[i][1]))
    else:
      # print the query
      speeds.append(speeds[-1])
      print("%s %.2f km" % (ins[i][0], sum(dists)))


if __name__ == '__main__':
  main()
