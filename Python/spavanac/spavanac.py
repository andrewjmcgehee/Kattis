ins = [int(i) for i in input().split()]

ins[1] -= 45

if ins[1] < 0:
    ins[1] += 60
    ins[0] -= 1
    if ins[0] < 0:
        ins[0] = 23

ins = [str(i) for i in ins]
print(' '.join(ins))
