minimum = int(input())
maxmimum = int(input())
target = int(input())

def get_sum(x):
    length = len(str(x))
    total = 0;
    for i in range(length, -1, -1):
        y = x // (10**i)
        total += y
        x -= y * 10**i
    return total

def main():
    small = None
    for i in range(minimum, maxmimum + 1):
        guess = get_sum(i)
        if guess == target:
            small = i
            break

    large = None
    for i in range(maxmimum, minimum - 1, -1):
        guess = get_sum(i)
        if guess == target:
            large = i
            break

    print(small)
    print(large)

if __name__ == '__main__':
    main()
