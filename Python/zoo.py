# Rating: ~ 1.7 / 10
# Link: https://open.kattis.com/problems/zoo
# Complexity: O(N) for N animals
# Memory: O(N) for N animals

list_num = 1
while True:
  n = int(input())
  animals = dict()
  if n == 0:
    break
  for i in range(n):
    line = input().split()
    animal = line[-1].lower()
    if animal not in animals:
      animals[animal] = 0
    animals[animal] += 1

  print("List %i:" % list_num)
  for animal in sorted(animals):
    print("%s | %i" % (animal, animals[animal]))

  list_num += 1

