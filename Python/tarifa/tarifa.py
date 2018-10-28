import sys

x = int(sys.stdin.readline())
n = int(sys.stdin.readline())
total = x * (n + 1)
rollover = 0

for line in sys.stdin:
    diff = x - int(line)
    rollover += diff

rollover += x
sys.stdout.write(str(rollover) + '\n')
