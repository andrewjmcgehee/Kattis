# Rating: ~ 1.9 / 10
# Link: https://open.kattis.com/problems/baconeggsandspam
# Complexity: O(K * N log(N)) where K is number of keys and N is length of longest array value
# Memory: O(KN) where K is number of keys and N is length of longest array value

import fileinput

def main():
  while True:
    num_orders = int(input())
    if num_orders == 0:
      break
    menu = dict()
    for i in range(num_orders):
      order = input().split()
      for item in order[1:]:
        if item not in menu:
          menu[item] = []
        menu[item].append(order[0])
    # sort foods and people
    foods = []
    for food in menu:
      menu[food].sort()
      foods.append(food)
    foods.sort()
    for food in foods:
      print(food, (' '.join(menu[food])))

if __name__ == '__main__':
    main()
