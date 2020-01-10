# Rating: ~ 3.5 / 10
# Link: https://open.kattis.com/problems/romanholidays

roms = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',
        10:'X',20:'XX',30:'XXX',40:'XL',50:'L',60:'LX',70:'LXX',80:'LXXX',
        90:'XC',100:'C',200:'CC',300:'CCC',400:'CD',500:'D',600:'DC',
        700:'DCC',800:'DCCC',900:'CM',1000:'M'}

def to_roman(i):
  out = []
  th = i // 1000
  r = i % 1000
  for _ in range(th):
    out.append(roms[1000])
  h = r // 100
  r = r % 100
  if h != 0:
    out.append(roms[h*100])
  t = r // 10
  r = r % 10
  if t != 0:
    out.append(roms[t*10])
  if r != 0:
    out.append(roms[r])
  return ''.join(out)

numerals = []
memo = dict()
for i in range(1, 1001):
  rom = to_roman(i)
  numerals.append(rom)
  memo[i] = rom
numerals.sort()

m_pos = -1
for i, num in enumerate(numerals):
  if num == 'M':
    m_pos = i
    break

def main():
  n = int(input())
  for _ in range(n):
    val = int(input())
    q = val // 1000
    r = val % 1000
    if val <= 1000:
      i = numerals.index(memo[val])
      if i > m_pos:
        print(-1 * (len(numerals)-i))
      else:
        print(i+1)
    else:
      if r == 0:
        print(q * (m_pos+1))
        continue
      i = numerals.index(memo[r])
      if i > m_pos:
        print(-1 * (len(numerals)-i) - q * (1000-m_pos-1))
      else:
        print(q * (m_pos+1) + i+1)

if __name__ == "__main__":
  main()
