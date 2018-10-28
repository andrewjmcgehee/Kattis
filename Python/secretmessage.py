def encrypt(message):
    L = len(message)
    K = pow(L, 0.5)
    if K % 1 != 0:
        K += 1
    K = int(K // 1)
    M = K**2

    message += '*' * (M-L)
    arr = [0 for i in range(len(message))]

    for i in range(len(message)):
        row = i % K
        col = K-1-(i//K)
        arr[(K*row) + col] = message[i]

    encrypted = ''
    for i in arr:
        if i != '*':
            encrypted += i
    return encrypted

def main():
    cases = int(input())
    output = ''
    for i in range(cases):
        message = input()
        output += encrypt(message)
        output += '\n'
    print(output)

if __name__ == '__main__':
    main()
