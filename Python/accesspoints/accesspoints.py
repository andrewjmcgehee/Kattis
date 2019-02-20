# Rating: ~ 5.4 / 10
# Link: https://open.kattis.com/problems/accesspoints
# Complexity: O(N) for N point ranges (this will approach NK by storing "ranges" smartly)
# Memory: O(N) for N points

def solve(coords, n):
  # first point always legal
  best = [(coords[0], 1)]
  for i in range(1, n):
    # add new point
    best.append((coords[i], 1))
    for j in range(len(best)-1, 0, -1):
      curr, num_curr = best[j]
      prev, num_prev = best[j-1]
      # legal move, point is to the right
      if curr > prev:
        break
      # find new location which is average of points
      num_items = num_curr + num_prev
      avg = curr*num_curr + prev*num_prev
      avg /= num_items
      # merge previous two ranges and continue
      best.pop()
      best.pop()
      best.append((avg, num_items))
  return best

# helper function to expand ranges back to points
def expand_points(x, y):
  x_res = []
  y_res = []
  for coord in x:
    x_res += [coord[0]] * coord[1]
  for coord in y:
    y_res += [coord[0]] * coord[1]
  return list(zip(x_res, y_res))

# helper function to calculate score
def get_score(targets, points, n):
  score = 0
  for i in range(n):
    x0, y0 = targets[i]
    xF, yF = points[i]
    score += (xF - x0)**2 + (yF - y0)**2
  return score

def main():
  n = int(input())
  x = []
  y = []
  for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

  # x and y can be solved independently because no shift in x
  # could ever cause a problem of order in the y axis
  x_coords = solve(x, n)
  y_coords = solve(y, n)
  coords = expand_points(x_coords, y_coords)
  points = list(zip(x, y))
  score = get_score(points, coords, n)
  print(score)

if __name__ == "__main__":
  main()
