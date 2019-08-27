/*
Rating: ~ 4.9 / 10
Link: https://open.kattis.com/problems/nonprimefactors
Complexity: O(N) where N is the maximum number for query
Memory: O(N) where N is the maximum number for query
*/

#include <iostream>
#include <string>
#include <vector>

#include <math.h>

using namespace std;

typedef long long ll;

void fast() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
}

// counts the number of times that a prime factor i can evenly go into a 
// number j
int count(int j, int i) {
  int sum = 0;
  while (j % i == 0) {
    sum++;
    j /= i;
  }
  return sum;
}

int MAX = 2000001;

int main() {
  fast();
  // index i gives total number of factors for the number i
  vector<ll> factors(MAX, 1);
  // index i gives the number of prime factors for the number i
  vector<ll> prime_factors(MAX, 0);
  
  // prime sieve plus updating the counts of factors and prime factors
  for (int i = 2; i < MAX; i++) {
    if (prime_factors[i] == 0) {
      for (int j = 2*i; j < MAX; j += i) {
        // every multiple will have j as a prime factor
        prime_factors[j]++;
        // 
        factors[j] *= (1 + count(j, i));
      }
    }
  }
  // handle cases
  int q;
  cin >> q;
  while (q--) {
    int n;
    cin >> n;
    cout << factors[n] - prime_factors[n] << '\n';
  }
  return 0;
}
