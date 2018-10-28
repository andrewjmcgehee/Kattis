from sys import stdin, stdout

n = int(stdin.readline().strip())

for i in range(n):
    args = [int(x) for x in stdin.readline().split()]
    x = args[0]
    y = args[1]
    z = args[2]
    
    if y - z > x:
        stdout.write('advertise\n')
    elif y - z == x:
        stdout.write('does not matter\n')
    else:
        stdout.write('do not advertise\n')
