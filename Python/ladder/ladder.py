import math
ins = [int(x) for x in input().split()]

print(math.ceil(ins[0] / math.sin(math.radians(ins[1]))))