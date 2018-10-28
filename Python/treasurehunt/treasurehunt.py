import sys

args = [int(x) for x in sys.stdin.readline().split()]


def hunt(r, c):
    treasure_map = []
    steps = 0
    row = 0
    col = 0
    been = {}
    been[row,col] = True

    for i in range(r):
        treasure_map.append(sys.stdin.readline().strip())

    while True:
        if treasure_map[row][col] == 'N':
            row -= 1
        elif treasure_map[row][col] == 'S':
            row += 1
        elif treasure_map[row][col] == 'W':
            col -= 1
        elif treasure_map[row][col] == 'E':
            col += 1
        elif treasure_map[row][col] == 'T':
            sys.stdout.write(str(steps) + '\n')
            break

        if row < 0 or col < 0 or row >= r or col >= c:
            sys.stdout.write('Out\n')
            break

        if (row,col) in been:
            if been[row,col]:
                sys.stdout.write('Lost\n')
                break

        steps += 1
        been[row,col] = True

hunt(args[0], args[1])
