/*
Rating: ~ 3.7 / 10
Link: https://open.kattis.com/problems/smallschedule
Complexity: O(N) for N total seconds
Memory: O(1)
*/

#include <iostream>
#include <string>
#include <vector>
using namespace std;

typedef long long ll;

// fast I/O
void fast() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
}

int main() {
  fast();
  // q-seconds, num machines, num 1 second slots, num q-second slots
  int q, m, s, l;
  cin >> q >> m >> s >> l;
  // total q-second slots to be handled
  int num_long_secs = l * q;

  int time = 0;
  while (num_long_secs > 0 || s > 0) {
    // greedy strategy
    if (num_long_secs > 0) {
      time += q;
      // try each machine
      for (int i = 0; i < m; i++) {
        // reduce number of q-second slots to be handled
        if (num_long_secs > 0) {
          num_long_secs -= q;
        }
        else {
          // each 1 second slot can handle q tasks in the meantime
          s -= q;
        }
      }
    }
    // 1 second per interval
    else {
      // m machines doing 1 task
      time++;
      s -= m;
    }
  }
  cout << time << '\n';
  return 0;
}
