# Rating: ~ 3.1 / 10
# Link: https://open.kattis.com/problems/color
# Complexity: O(N) for N socks
# Memory: O(N) for N socks

def main():
  # inputs
  s, c, k = map(int, input().split())
  # get socks and sort them
  socks = [int(x) for x in input().split()]
  socks.sort()

  machines = []
  i = 0
  # iterate grouping socks together greedily by minimum distances
  while i < len(socks):
    # each iteration will add a new "machine"
    machines.append([socks[i]])
    i += 1
    # must have no more than C socks in a machine
    while i < len(socks) and len(machines[-1]) < c:
      # valid pair - note that first pair in machine will have lowest
      # color value and thus furthest distance as more socks are added
      if abs(socks[i] - machines[-1][0]) <= k:
        machines[-1].append(socks[i])
        i += 1
      # invalid pair
      else:
        break
  print(len(machines))




if __name__ == "__main__":
  main()
