# Rating: ~ 2.0 / 10
# Link: https://open.kattis.com/problems/measurement

to_short = {
  'thou': 'th',
  'inch': 'in',
  'foot': 'ft',
  'yard': 'yd',
  'chain': 'ch',
  'furlong': 'fur',
  'mile': 'mi',
  'league': 'lea'
}
to_index = {'th':0, 'in':1, 'ft':2, 'yd':3, 'ch':4, 'fur':5, 'mi':6, 'lea':7}
conv = [1000, 12, 3, 22, 10, 8, 3]
def main():
  val, u, _, v = input().split()
  val = int(val)
  if len(u) > 3:
    u = to_short[u]
  if len(v) > 3:
    v = to_short[v]
  u_index = to_index[u]
  v_index = to_index[v]
  if u_index == v_index:
    print(1)
    return
  if u_index < v_index:
    for i in range(u_index, v_index):
      val /= conv[i]
    print(val)
  else:
    for i in range(v_index, u_index):
      val *= conv[i]
    print(val)


if __name__ == "__main__":
  main()
