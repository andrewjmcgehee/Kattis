import fileinput
import math


def factors(num):
    prime_factors = dict()
    for i in range(2, math.ceil(math.sqrt(num) + 1)):
        while num % i == 0:
            if i not in prime_factors:
                prime_factors[i] = 0
            prime_factors[i] += 1
            num //= i
    if num > 1:
        if num not in prime_factors:
            prime_factors[num] = 0
        prime_factors[num] += 1
    return prime_factors;



def merge(map1,map2):
    for i in map2:
        if i not in map1:
            map1[i] = 0
        map1[i] = max(map1[i], map2[i]);
    return map1


def main():
    for line in fileinput.input():
        arr = [int(x) for x in line.split()]

        map1 = factors(arr[0])
        for i in range(1, len(arr)):
            map2 = factors(arr[i])
            map1 = merge(map1, map2)

        solution = 1;
        for i in map1:
            for j in range(map1[i]):
                solution *= i
        print(solution)

if __name__ == '__main__':
    main()
