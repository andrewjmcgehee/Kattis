# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/aliennumbers
# Complexity: O(N) for N digits to be processed
# Memory: O(N) for N digits to map to and from

def main():
  n = int(input())
  for case in range(1, n+1):
    num, source, target = (x for x in input().split())

    # maps a source character to a base 10 number
    source_digs = dict()
    for i, v in enumerate(source):
      source_digs[v] = i

    # maps a base 10 number to a target character
    target_digs = dict()
    for i, v in enumerate(target):
      target_digs[i] = v

    # convert to decimal first
    dec_number = 0
    alien_base = len(source)
    for i in range(len(num)-1, -1, -1):
      power = len(num)-i-1
      coefficient = source_digs[num[i]]
      dec_number += coefficient * pow(alien_base, power)

    # convert to target language
    out_num = ''
    target_base = len(target)
    while dec_number:
      # get one digit at a time
      rem = dec_number % target_base
      val = target_digs[rem]
      # prepend it
      out_num = val + out_num
      dec_number = dec_number // target_base
    print("Case #%i: %s" % (case, out_num))

if __name__ == '__main__':
  main()

