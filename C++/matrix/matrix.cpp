/*
Rating: ~ 3.4 / 10
Link: https://open.kattis.com/problems/matrix
Complexity: O(1)
Memory: O(1)
*/

#include <iostream>
using namespace std;

typedef long long ll;

void fast() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
}

int main() {
  // fast I/O
  fast();
  int a, b, c, d;
  int case_num = 1;
  while (cin >> a) {
    cin >> b >> c >> d;
    // calculate determinant
    int det = a * d - b * c;
    cout << "Case " << case_num << ":\n";

    // Follows the form
    // [  d -b ]
    // [ -c  a ]
    cout << d / det << " " << -1*b / det << '\n';
    cout << -1*c / det << " " << a / det << '\n';
    // white space
    cin.ignore();
    case_num++;
  }
  return 0;
}
