num = list(str(input()))
num = num[::-1]
remainder = None
stem = None
# All digit characters less than 'A'
MAX = 'A'

for x in range(len(num)-1):
    if num[x+1] < num[x]:
        swap = MAX
        location = None
        for i, v in enumerate(num[:x+1]):
            if v > num[x+1] and v < swap:
                swap = v
                location = i

        num[x+1], num[location] = num[location], num[x+1]
        remainder = num[:x+1]
        stem = num[x+1:]
        stem = stem[::-1]
        break

if remainder:
    remainder.sort()
    stem.extend(remainder)
    print(''.join(stem))
else:
    print(0)
