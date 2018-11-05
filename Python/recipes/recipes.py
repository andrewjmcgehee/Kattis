# Rating: ~ 1.9 / 10
# Link: https://open.kattis.com/problems/recipes
# Complexity: O(N) for N ingredients
# Memory: O(N) for N ingredients

from collections import OrderedDict

def main():
  t = int(input())
  # test cases
  for case in range(1, t+1):
    # num ingredients, portions, desired portions
    r, p, d = map(int, input().split())

    # scalar
    scale = d / p
    scaled_weight = None

    # holds ingredients in order of insertion
    ingred = OrderedDict()
    for i in range(r):
      # name, weight, percent
      name, w, per = [x for x in input().split()]
      w = float(w)
      per = float(per) / 100
      # the chosen scaling ingredient
      if per == 1.0:
        scaled_weight = scale * w
      ingred[name] = per

    print("Recipe # %i" % case)
    for item in ingred:
      # print out scaled ingredients
      print("%s %.1f" % (item, scaled_weight * ingred[item]))
    print('-' * 40)

if __name__ == '__main__':
  main()


