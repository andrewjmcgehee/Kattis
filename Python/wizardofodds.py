import math

def main():
    ins = [int(n) for n in input().split()]
    n = ins[0]
    k = ins[1]
    num_guesses = math.log2(n)
    if num_guesses > k:
        print('You will become a flying monkey!')
    else:
        print('Your wish is granted!')

if __name__ == '__main__':
    main()
