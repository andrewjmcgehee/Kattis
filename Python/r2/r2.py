import sys

args = [int(x) for x in sys.stdin.readline().split()]

r1 = args[0]
s1 = args[1]

r2 = s1 * 2
r2 -= r1

sys.stdout.write(str(r2) + '\n')
