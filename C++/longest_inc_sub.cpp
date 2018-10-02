/*
Rating: ~ 5.2 / 10
Link: https://open.kattis.com/problems/longincsubseq
Complexity: O(N log(N)) due to N calls to binary search O(log(N))
Memory: O(N) for N values
*/

#include <bits/stdc++.h>
using namespace std;

// binary search helper for placing interior nodes of longest subseq
int bin_search(vector<int> &arr, vector<int> &tail, int left, int right, int key) {
  while (right - left > 1) {
    int mid = left + (right - left)/2;
    if (arr[tail[mid]] >= key) {
      right = mid;
    }
    else {
      left = mid;
    }
  }
  return right;
}

// longest increasing subseq method
vector<int> lis(vector<int> &arr) {
  int n = arr.size();
  // keeps last element of current longest subseq
  vector<int> tail(n, 0);
  // stores index of previous element in sequence
  vector<int> prev(n, -1);

  int len = 1;
  for (int i = 1; i < n; i++) {
    if (arr[i] < arr[tail[0]]) {
      // new start candidate
      tail[0] = i;
    }
    else if (arr[i] > arr[tail[len-1]]) {
      // arr[i] extends largest subsequence
      prev[i] = tail[len-1];
      tail[len++] = i;
    }
    else {
      // arr[i] replaces interior value of smaller sequence
      int pos = bin_search(arr, tail, -1, len-1, arr[i]);
      prev[i] = tail[pos-1];
      tail[pos] = i;
    }
  }

  // build indices of longest sequence
  vector<int> longest;
  for (int i = tail[len-1]; i >= 0; i = prev[i]) {
    if (arr[i] != arr[prev[i]]) {
      longest.push_back(i);
    }
  }
  reverse(longest.begin(), longest.end());
  return longest;
}

int main() {
  int n;
  while (cin >> n) {
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
      cin >> arr[i];
    }
    vector<int> solution = lis(arr);
    cout << solution.size() << '\n';
    for (int i : solution) {
      cout << i << ' ';
    }
    cout << '\n';
  }
}
