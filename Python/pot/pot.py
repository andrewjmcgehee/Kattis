from sys import stdin, stdout

test_cases = int(stdin.readline());
result = 0

for line in stdin:
    line = line.strip()
    result += int(line[:-1])**int(line[-1])

stdout.write(str(result) + '\n')
