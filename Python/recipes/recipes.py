from collections import OrderedDict

def main():
  t = int(input())
  for case in range(1, t+1):
    r, p, d = [int(x) for x in input().split()]

    scale = d / p
    scaled_weight = None

    ingred = OrderedDict()
    for i in range(r):
      name, w, per = [x for x in input().split()]
      w = float(w)
      per = float(per) / 100
      if per == 1.0:
        scaled_weight = scale * w
      ingred[name] = per

    print("Recipe # %i" % case)
    for item in ingred:
      print("%s %.1f" % (item, scaled_weight * ingred[item]))
    print('-' * 40)

if __name__ == '__main__':
  main()


