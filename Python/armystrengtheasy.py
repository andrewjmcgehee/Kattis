# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/armystrengtheasy
# Complexity: O(N log(N)) to sort N items where N is size of larger army
# Memory: O(N + M) to store N and M soldiers

def main():
  t = int(input())
  for _ in range(t):
    # trash unnecessary inputs
    ws = input()
    sizes = input()
    god = [int(x) for x in input().split()]
    mecha = [int(x) for x in input().split()]
    # sorts soldiers weakest to strongest
    god.sort()
    mecha.sort()

    # while each pseudo queue is not empty
    while god and mecha:
      # python for treating an array as a queue, pop the weaker soldier
      if god[0] < mecha[0]:
        del god[0]
      else:
        del mecha[0]
    if god:
      print('Godzilla')
    else:
      print('Mechagodzilla')

if __name__ == '__main__':
  main()

