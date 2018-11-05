# Rating: ~ 3.9 / 10
# Link: https://open.kattis.com/problems/smallestmultiple
# Complexity: O(N sqrt(K)) for N numbers and getting prime factors 1 thru K
# Memory: O(N) for N factors

import fileinput
import math

# get prime factors of a given number
def factors(num):
  prime_factors = dict()
  for i in range(2, math.ceil(math.sqrt(num) + 1)):
    # while divisible by a prime divide it and increment frequency
    while num % i == 0:
      if i not in prime_factors:
        prime_factors[i] = 0
      prime_factors[i] += 1
      num //= i
  # prime factor as remainder
  if num > 1:
    if num not in prime_factors:
      prime_factors[num] = 0
    prime_factors[num] += 1
  return prime_factors

# merges two maps of factors by taking the maximum occurences of each
def merge(map1,map2):
  for i in map2:
    # check for key errors
    if i not in map1:
      map1[i] = 0
    map1[i] = max(map1[i], map2[i]);
  return map1


def main():
  for line in fileinput.input():
    # get all factors
    arr = [int(x) for x in line.split()]

    # count frequencies of prime factors
    map1 = factors(arr[0])
    for i in range(1, len(arr)):
      # merge primes factors of each of the other numbers in the list
      map2 = factors(arr[i])
      map1 = merge(map1, map2)

    solution = 1;
    for i in map1:
      # for each prime factor multiple by it the number of times it
      # occurs in the new number
      for j in range(map1[i]):
        solution *= i
    print(solution)

if __name__ == '__main__':
    main()
