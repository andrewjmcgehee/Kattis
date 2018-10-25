/*
Rating: ~ 5.0 / 10
Link: https://open.kattis.com/problems/primesieve
Complexity: O(sqrt(N))
Memory: O(N) for N booleans storing if index K is prime
*/

#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

int main() {
  // inputs
  int n, q;
  cin >> n >> q;

  // sieve
  vector<bool> is_prime(n+1, true);
  // 0 and 1 not prime
  is_prime[0] = false;
  is_prime[1] = false;
  // num_primes would start at n + 1 (including 0 and 1) but removing them
  // makes it n-1. now we can simply start at 2, like a traditional sieve
  int num_primes = n-1;
  for (int i = 2; i*i <= n; i++) {
    if (is_prime[i]) {
      for (int j = i*i; j < n+1; j += i) {
        if (is_prime[j]) {
          is_prime[j] = false;
          num_primes--;
        }
      }
    }
  }
  // number of primes
  cout << num_primes << '\n';
  // handle queries
  for (int i = 0; i < q; i++) {
    int query;
    cin >> query;
    if (is_prime[query]) {
      cout << 1 << '\n';
      continue;
    }
    cout << 0 << '\n';
  }
  return 0;
}
