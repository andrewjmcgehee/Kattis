items = int(input())

while items != 0:
    a = []
    b = []
    for i in range(items):
        a.append(int(input()))
    for i in range(items):
        b.append(int(input()))
    c = sorted(a)
    d = sorted(b)
    table = dict()
    for i in range(items):
        table[c[i]] = d[i]
    for i in range(items):
        print(table[a[i]])

    print()
    items = int(input())
