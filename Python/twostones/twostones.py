from sys import stdin, stdout

def main():
    i = int(stdin.readline().strip())
    if i % 2 == 0:
        stdout.write('Bob\n')
    else:
        stdout.write('Alice\n')

if __name__ == '__main__':
    main()
