from sys import stdin, stdout

n = int(stdin.readline().strip())

for i in range(n):
    x = int(stdin.readline().strip())
    if x % 2 == 0:
        stdout.write(str(x) + ' is even\n')
    else:
        stdout.write(str(x) + ' is odd\n')
