# Rating: ~ 1.9 / 10
# Link: https://open.kattis.com/problems/3dprinter
# Complexity: O(1)
# Memory: O(1)

def main():
    printers = 1
    statues = int(input())

    # always smarter to double printers and print all in one day
    # as 2^n grows fasters than linear production
    i = 0
    while 2**i < statues:
        i += 1

    # 1 extra day to actually print
    days = i + 1
    print(days)

if __name__ == '__main__':
    main()
