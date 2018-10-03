# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/batterup
# Complexity: O(N) for N items
# Memory: O(1)

_ = input()
ins = [int(i) for i in input().split()]

divisor = 0
numerator = 0
for i in ins:
  # if i is meaningful add it to numerator and increment denominator
  if i >= 0:
    numerator += i
    divisor += 1

print(numerator / divisor)
