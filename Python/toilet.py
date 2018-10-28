def main():
    line = input()

    up = 0
    down = 0
    found = 0

    # UU
    # DD
    # UD
    # DU

    for i in range(1, len(line)):
        if i == 1:
            if line[0] == 'U' and line[1] == 'D':
                up += 2
            elif line[0] == 'D':
                up += 1
        elif line[i] == 'D':
            up += 2

    for i in range(1, len(line)):
        if i == 1:
            if line[0] == 'D' and line[1] == 'U':
                down += 2
            elif line[0] == 'U':
                down += 1
        elif line[i] == 'U':
            down += 2

    for i in range(1, len(line)):
        if line[i] != line[i-1]:
            found += 1

    print(up)
    print(down)
    print(found)

if __name__ == '__main__':
    main()
