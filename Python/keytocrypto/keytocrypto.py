from sys import stdin, stdout

def main():
    SHIFTS = {'A':0, 'B':1, 'C':2, 'D':3,
              'E':4, 'F':5, 'G':6, 'H':7,
              'I':8, 'J':9, 'K':10, 'L':11,
              'M':12, 'N':13, 'O':14, 'P':15,
              'Q':16, 'R':17, 'S':18, 'T':19,
              'U':20, 'V':21, 'W':22, 'X':23,
              'Y':24, 'Z':25}

    cipher = stdin.readline().strip()
    keytxt = stdin.readline().strip()
    translation = []
    current_index = 0
    result = ''

    for i in range(len(keytxt)):
        translation.append(SHIFTS[keytxt[i]])
        current_index += 1

    i = 0
    while True:
        if len(result) == len(cipher):
            break
        else:
            if SHIFTS[cipher[i]] - translation[i] >= 0:
                result += chr(ord(cipher[i]) - translation[i])
            else: 
                result += chr(ord(cipher[i]) - translation[i] + 26)
            translation.append(SHIFTS[result[i]])
            i += 1

    print(result)
        
    
    

if __name__ == '__main__':
    main()


