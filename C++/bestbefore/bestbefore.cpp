/*
Rating: ~ 3.4 / 10
Link: https://open.kattis.com/problems/bestbefore
Complexity: O(N!) for N date fields (only 3)
Memory: O(1)
*/

#include <algorithm>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

typedef long long ll;

// fast IO
void fast() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
}

// helper function to check leap year as defined by problem
bool is_leap_year(int year) {
  if (year % 4 == 0) {
    if (year % 100 == 0 && year % 400 != 0) return false;
    return true;
  }
  return false;
}

// number of days in each month
const vector<int> DAYS = {31,28,31,30,31,30,31,31,30,31,30,31};

bool is_valid_date(vector<int> date) {
  // make year in 2000s range
  if (date[0] < 2000) date[0] += 2000;
  // greater than december
  if (date[1] > 12) return false;
  // number of days in the month
  int num_days = DAYS[date[1]-1];
  // one extra for feb in leap year
  if (date[1] == 2 && is_leap_year(date[0])) num_days++;
  // too many days
  if (date[2] > num_days) return false;
  return true;
}

string build_date(vector<int> date) {
  // make year in 2000s range
  if (date[0] < 2000) date[0] += 2000;
  string s = to_string(date[0]) + '-';
  // pad with 0 if less than 10
  if (date[1] < 10) s += '0';
  s += to_string(date[1]) + '-';
  if (date[2] < 10) s += '0';
  s += to_string(date[2]);
  return s;
}

int main() {
  fast();
  string line;
  getline(cin, line);
  stringstream ss(line);

  vector<int> date(3);
  bool possible = true;
  // get values
  for (int i = 0; i < 3; i++) {
    ss >> date[i];
    // ignore slashes
    ss.ignore();
    // cant have negative options
    if (date[i] < 0) possible = false;
    // make year in 2000s range
    if (date[i] == 0) date[i] += 2000;
  }
  sort(date.begin(), date.end());

  // try all permutations
  vector<string> solutions;
  do {
    if (is_valid_date(date)) {
      solutions.push_back(build_date(date));
    }
  } while (next_permutation(date.begin(), date.end()));
  // sort solutions
  sort(solutions.begin(), solutions.end());

  // valid inputs and solution found
  if (possible && solutions.size() != 0) {
    cout << solutions[0] << '\n';
    return 0;
  }
  cout << line << " is illegal\n";
  return 0;
}

