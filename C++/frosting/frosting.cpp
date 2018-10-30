/*
Rating: ~ 3.4 / 10
Link: https://open.kattis.com/problems/frosting
Complexity: O(N + K) for N rows and K columns
Memory: O(N + K) for N rows and K columns
*/

#include <iostream>
#include <string>
#include <vector>
using namespace std;

typedef long long ll;

// faster i/o
void fast() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
}

int main() {
  fast();
  int n;
  cin >> n;

  vector<ll> cols(3, 0);
  for (int i = 0; i < n; i++) {
    ll col;
    cin >> col;
    // each color will initially have the sum of all the column sizes
    // as a side length
    cols[i%3] += col;
  }

  vector<ll> areas(3, 0);
  for (int i = 0; i < n; i++) {
    ll row;
    cin >> row;
    // calculate total areas by multiplying sidelength by applicable
    // row sizes and summing
    areas[i%3] += cols[i%3] * row;
    areas[(i+1)%3] += cols[(i+2)%3] * row;
    areas[(i+2)%3] += cols[(i+1)%3] * row;
  }
  cout << areas[2] << ' ' << areas[1] << ' ' << areas[0] << '\n';
}
