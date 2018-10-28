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
  boys = sorted([int(x) for x in input().split()])
  a, b = (int(x) for x in input().split())
  # force a and b to be odd
  if a & 1 == 0:
    a += 1
  if b & 1 == 0:
    b -= 1

  best = a
  a_distance = abs(find_nearest(a, boys)-a)
  best_distance = a_distance
  b_distance = abs(find_nearest(b, boys)-b)
  if b_distance > a_distance:
    best_distance = b_distance
    best = b

  for i in range(n-1):
    midpoint = (boys[i] + boys[i+1]) // 2
    if midpoint & 1 == 0:
      midpoint -= 1
    if midpoint < a:
      continue
    if midpoint > b:
      break
    distance = abs(midpoint - boys[i])
    if distance > best_distance:
      best_distance = distance
      best = midpoint
  print(best)

if __name__ == '__main__':
  main()
