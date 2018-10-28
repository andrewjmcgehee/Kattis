def main():
    from sys import stdin, stdout
    while True:
        ins = stdin.readline()

        if ins[0] == '0':
            break

        ins = [int(x) for x in ins.split()]
        n = ins[0]
        k = ins[1]

        if n == 1:
            stdout.write('-\n')
            continue

        wins = dict()
        losses = dict()
        for i in range(1, n+1):
            wins[i] = 0
            losses[i] = 0

        for i in range(int(k * n*(n-1)/2)):
            match = stdin.readline().split()
            p1 = int(match[0])
            m1 = match[1][0]
            p2 = int(match[2])
            m2 = match[3][0]
            if m1 == 'r':
                if m2 == 'p':
                    wins[p2] += 1
                    losses[p1] += 1
                elif m2 == 's':
                    wins[p1] += 1
                    losses[p2] += 1
            elif m1 == 'p':
                if m2 == 's':
                    wins[p2] += 1
                    losses[p1] += 1
                elif m2 == 'r':
                    wins[p1] += 1
                    losses[p2] += 1
            else:
                if m2 == 'r':
                    wins[p2] += 1
                    losses[p1] += 1
                elif m2 == 'p':
                    wins[p1] += 1
                    losses[p2] += 1

        for i in range(1, n+1):
            if wins[i] + losses[i] == 0:
                stdout.write('-\n')
                continue
            stdout.write(format(wins[i] / (wins[i] + losses[i]), ".3f"))
            stdout.write('\n')

if __name__ == '__main__':
    main()

