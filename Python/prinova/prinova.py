# Rating: ~ 4.8 / 10
# Link: https://open.kattis.com/problems/prinova
# Complexity: O(N) for N boys
# Memory: O(N) for N boys

# helper function to find nearest boy for end points of range
def find_nearest(value, boys):
  closest = None
  current = 10000000000
  for boy in boys:
    if abs(value-boy) < current:
      current = abs(value-boy)
      closest = boy
  return closest

def main():
  n = int(input())
  # get boys and sort them
  boys = sorted([int(x) for x in input().split()])
  a, b = map(int, input().split())
  # force a and b to be odd
  if a & 1 == 0:
    a += 1
  if b & 1 == 0:
    b -= 1

  # distance from lowest number in range - best initially starts here
  best = a
  a_distance = abs(find_nearest(a, boys)-a)
  best_distance = a_distance
  # distance from largest number in range
  b_distance = abs(find_nearest(b, boys)-b)
  if b_distance > a_distance:
    best_distance = b_distance
    best = b

  # try in between each boy
  for i in range(n-1):
    # get mid point (max distance between the two points
    midpoint = (boys[i] + boys[i+1]) // 2
    # force it to be odd
    if midpoint & 1 == 0:
      midpoint -= 1
    # check range bounds
    if midpoint < a:
      continue
    if midpoint > b:
      break
    # get distance
    distance = abs(midpoint - boys[i])
    # check if better
    if distance > best_distance:
      best_distance = distance
      best = midpoint
  print(best)

if __name__ == '__main__':
  main()
