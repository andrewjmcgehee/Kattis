# Rating: ~ 2.4 / 10
# Link: https://open.kattis.com/problems/permutationencryption
# Complexity: O(N) for N characters in string
# Memory: O(N) for N characters in string

def main():
  while True:
    line = [int(i) for i in input().split()]
    if line[0] == 0:
      break

    # get key
    key_len = line[0]
    key = line[1:]
    # compensate for 1 indexing
    for i in range(len(key)):
      key[i] -= 1

    # make string mutable
    message = list(input())
    length = len(message)
    # pad with spaces at the end to make key fit evenly
    while length % key_len != 0:
      message.append(' ')
      length += 1

    # number of discrete sections
    num_parts = length // key_len
    ans = []
    for i in range(num_parts):
      # get a single part
      part = message[key_len*i:key_len*(i+1)]
      encrypted = []
      for index in key:
        # get the character at the shifted index
        encrypted.append(part[index])
      ans.append(''.join(encrypted))
    print('\'%s\'' % ''.join(ans))

if __name__ == '__main__':
  main()
