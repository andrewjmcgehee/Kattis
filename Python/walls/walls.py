# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/walls
# Complexity: O(2^N) for N cranes ( <= 30 )
# Memory:

# initially 5 because all 4 cranes can be covered with 4 bits
best = 5

def search(covered, count, matches):
  global best

  # no remaining elements to process
  if len(covered) == 0:
    # will equal 15 if all 4 bits are a 1 and count stores number
    # of cranes included
    if matches == 15 and count < best:
      best = count
    return
  # get first value
  val = covered[0]
  # remaining cranes
  covered = covered[1:]
  # include crane
  search(covered, count+1, matches | val)
  # dont include
  search(covered, count, matches)

def main():
  l, w, n, r = map(int, input().split())
  centers = [(l/2.0, 0), (-1*l/2.0, 0), (0, w/2.0), (0, -1*w/2.0)]

  # will hold coverage of each crane
  covered = set()
  for i in range(n):
    x, y = map(int, input().split())
    match = 0
    for j in range(4):
      cx, cy = centers[j]
      dx = (cx-x)**2
      dy = (cy-y)**2
      # in radius, use squared distance to stay in integers
      if r**2 >= dx + dy:
        match |= 2**j
    if match:
      covered.add(match)
  # search begins with whole list, 0 cranes, and 0 matched bits)
  search(list(covered), 0, 0)
  if best == 5:
    print("Impossible")
  else:
    print(best)


if __name__ == "__main__":
  main()
