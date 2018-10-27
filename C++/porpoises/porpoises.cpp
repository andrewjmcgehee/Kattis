/*
Rating: ~ 3.1 / 10 (yeah... right)
Link: https://open.kattis.com/problems/porpoises
Complexity: O(log N) due to arithmetic fibonacci method
Memory: O(N) for memo table
*/

#include <cstdio>
#include <map>
using namespace std;

const long long MOD = 1000000000;
typedef long long ll;

map<ll, ll> memo;

// some fibonacci magic I found online. Calculates nth fibonacci number in O(log N)
// time
ll fib(ll n) {
  if (n == 0) return 0;
  if (n == 1 || n == 2) {
    memo[n] = 1;
    return 1;
  }
  if (memo.find(n) != memo.end()){
    return memo[n];
  }

  ll tmp;
  if (n % 2 == 0) {
    tmp = n / 2;
    memo[n] = fib(tmp) * (fib(tmp) + 2*fib(tmp-1));
    memo[n] %= MOD;
  }
  else {
    tmp = (n+1) / 2;
    memo[n] = fib(tmp)*fib(tmp) + fib(tmp-1)*fib(tmp-1);
    memo[n] %= MOD;
  }
  return memo[n];
}

int main() {
  memo[0] = 0;
  memo[1] = 1;

  int p;
  scanf("%d", &p);
  for (int i = 0; i < p; i++) {
    int n;
    ll m;
    scanf("%d %lld", &n, &m);
    ll answer = fib(m);
    printf("%d %lld\n", i+1, answer);
  }
  return 0;
}
