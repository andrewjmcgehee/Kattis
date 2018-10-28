n = int(input())

while n != -1:
    board = []
    for i in range(n):
        board.append([int(x) for x in input().split()])

    neighbors = dict()
    for i in range(n):
        neighbors[i] = set()
        for j in range(n):
            if board[i][j] == 1:
                neighbors[i].add(j)

    weak = []

    for i in range(n):
        is_strong = False
        n1 = neighbors[i]
        for j in n1:
            n2 = neighbors[j] - {i}
            for k in n2:
                n3 = neighbors[k] - {j}
                if i in n3:
                    is_strong = True
                    break
            if is_strong:
                break
        if not is_strong:
            weak.append(str(i))
    print(" ".join(weak))
    n = int(input())

