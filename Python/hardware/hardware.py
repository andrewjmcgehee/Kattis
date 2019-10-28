# Rating: ~ 2.1 / 10
# Link: https://open.kattis.com/problems/hardware

def main():
  n = int(input())
  for i in range(n):
    address = input()
    second_line = input()
    num_signs = int(second_line.split()[0])
    signs = []
    while len(signs) != num_signs:
      line = input()
      if line.startswith('+'):
        _, first, second, interval = line.split()
        for i in range(int(first), int(second)+1, int(interval)):
          signs.append(str(i))
      else:
        signs.append(line)

    freq = {i:0 for i in range(10)}
    for sign in signs:
      for i in range(10):
        freq[i] += sign.count(str(i))
    print(address)
    print(second_line)
    for i in range(10):
      print('Make {} digit {}'.format(freq[i], i))
    total = sum(freq.values())
    if total == 1:
      print('In total 1 digit')
    else:
      print('In total {} digits'.format(total))


if __name__ == "__main__":
  main()
