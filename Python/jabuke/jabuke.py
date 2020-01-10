# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/jabuke

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

def area(a, b, c):
  return abs(a.x*(b.y - c.y) + b.x*(c.y-a.y) + c.x*(a.y-b.y)) / 2

EPS = 1e-6

def main():
  x, y = map(int, input().split())
  A = Point(x, y)
  x, y = map(int, input().split())
  B = Point(x, y)
  x, y = map(int, input().split())
  C = Point(x, y)
  tri_area = area(A, B, C)
  trees = 0
  t = int(input())
  for _ in range(t):
    x, y = map(int, input().split())
    p = Point(x, y)
    p_area = area(p, A, B)
    p_area += area(p, B, C)
    p_area += area(p, A, C)
    if abs(p_area-tri_area) < EPS:
      trees += 1
  print('{:.1f}'.format(tri_area))
  print(trees)

if __name__ == "__main__":
  main()
