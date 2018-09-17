/*
Rating: ~ 2.9 / 10
Link: https://open.kattis.com/problems/averageshard
Complexity: O(n) where n is number of CS students
Memory: O(1)
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
  // I/O Optimization
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int num_cases;
  cin >> num_cases;

  for (int i = 0; i < num_cases; i++) {
    int num_cs;
    int num_econ;
    cin >> num_cs;
    cin >> num_econ;

    // get averages
    vector<int> cs;
    vector<int> econ;
    long long cs_sum = 0;
    long long econ_sum = 0;
    for (int j = 0; j < num_cs; j++) {
      int iq;
      cin >> iq;
      cs.push_back(iq);
      cs_sum += iq;
    }
    for (int j = 0; j < num_econ; j++) {
      int iq;
      cin >> iq;
      econ.push_back(iq);
      econ_sum += iq;
    }
    double cs_avg = cs_sum / double(num_cs);
    double econ_avg = econ_sum / double(num_econ);

    // trick is knowing that if CS score is less than CS avg and greater than Econ avg
    // then the student will improve both by switching
    int num_students = 0;
    for (int j = 0; j < num_cs; j++) {
      if (cs[j] < cs_avg && cs[j] > econ_avg) {
        num_students++;
      }
    }
    cout << num_students << '\n';
  }
  return 0;
}
