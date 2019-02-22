# Rating: ~ 3.4 / 10
# Link: https://open.kattis.com/problems/vegetables
# Complexity: O(K*N log(N)) for K sorts of N veggies
# Memory: O(N) for N veggies

# define precision desired
EPS = 0.000001

# vegetable class for ease of use over tuples
class Veg:
  def __init__(self, weight, index):
    self.weight = weight
    self.cuts = 0
    self.index = index

  # define comparable
  def __lt__(self, other):
    l = self.weight / (self.cuts+1)
    r = other.weight / (other.cuts+1)

    # compare by ratios first, then weight, then index
    if abs(l-r) < EPS:
      if self.weight == other.weight:
        return self.index < other.index
      return self.weight < other.weight
    return l < r

  def __str__(self):
    return str(self.weight) + ' ' + str(self.cuts)

# helper function to get ratio of two veggies
def ratio(a, b):
  lo = a.weight / (a.cuts+1)
  hi = b.weight / (b.cuts+1)
  return lo / hi

def main():
  line = input().split()
  # target ratio
  T = float(line[0])
  n = int(line[1])

  # get weights and create veggies
  weights = [int(x) for x in input().split()]
  veggies = []
  for i in range(n):
    v = Veg(weights[i], i)
    veggies.append(v)
  # sort to keep smallest at 0 and largest at len - 1
  veggies.sort()

  cuts = 0
  while ratio(veggies[0], veggies[-1]) < T:
    # cut larget into smaller even pieces
    v = veggies[-1]
    veggies.remove(v)
    v.cuts += 1
    cuts += 1
    veggies.append(v)
    # keep sorted for ratio
    veggies.sort()
  print(cuts)

if __name__ == "__main__":
  main()
