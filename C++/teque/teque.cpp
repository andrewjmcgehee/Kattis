/*
Rating: ~ 3.5 / 10
Link: https://open.kattis.com/problems/teque
*/

#include <deque>
#include <iostream>
#include <string>
using namespace std;

typedef long long ll;

deque<int> f;
deque<int> b;

void balance() {
  if (f.size() > b.size()) {
    b.push_front(f.back());
    f.pop_back();
    return;
  }
  if (b.size() > f.size()+1) {
    f.push_back(b.front());
    b.pop_front();
    return;
  }
}

int get(int index) {
  if (index < f.size()) return f[index];
  index -= f.size();
  return b[index];
}

void pushback(int val) {
  b.push_back(val);
  balance();
}

void pushfront(int val) {
  f.push_front(val);
  balance();
}

void pushmiddle(int val) {
  if (f.size() == b.size()) b.push_front(val);
  else {
    f.push_back(b.front());
    b.pop_front();
    b.push_front(val);
  }
}

void fast() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
}

int main() {
  fast();
  int cmds;
  cin >> cmds >> ws;

  while (cmds--) {
    string c;
    int val;
    cin >> c >> val >> ws;
    if (c == "get") {
      int i = get(val);
      cout << i << '\n';
    } else {
      if (c[5] == 'b') {
        pushback(val);
      }
      if (c[5] == 'm') {
        pushmiddle(val);
      }
      if (c[5] == 'f') {
        pushfront(val);
      }
    }
  }
  return 0;
}
