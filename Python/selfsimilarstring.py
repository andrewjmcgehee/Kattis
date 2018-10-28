import fileinput

def main():
    for line in fileinput.input():
        length = len(line)
        max_degree = 0
        similar = True
        while (similar):
            degree = max_degree + 1
            tokens = dict()
            for i in range(length - degree):
                token = line[i:i+degree]
                if token not in tokens:
                    tokens[token] = 1
                else:
                    tokens[token] += 1
            for token in tokens:
                if tokens[token] < 2:
                    similar = False
                    break
            if not similar:
                break
            max_degree = degree
        print(max_degree)

if __name__ == '__main__':
    main()
