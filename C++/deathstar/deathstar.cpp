/*
Rating: ~ 2.0 / 10
Link: https://open.kattis.com/problems/deathstar
*/

#include <iostream>
#include <string>
#include <vector>
using namespace std;

typedef long long ll;

void fast() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
}

int main() {
  int n;
  cin >> n;
  vector<int> diag(n, 0);
  for (int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      int num;
      cin >> num;
      diag[i] |= num;
    }
  }
  for (int i = 0; i < n; i++) cout << diag[i] << " ";
  cout << '\n';
  return 0;
}
