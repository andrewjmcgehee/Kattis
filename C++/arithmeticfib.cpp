/*
This is a not a solution to a kattis problem.

This is simply a cool way to calculate the nth fibonacci
number based on arithmetic sequences. I used this to solve
Immortal Porpoises on Kattis.
*/

#include <cstdio>
using namespace std;

const int MAX = 1000;
long long memo[MAX] = {0};

long long fib(int n) {
  if (n == 0) return 0;
  if (n == 1) return 1;
  if (memo[n]) return memo[n];

  // if n is even or odd
  int k = (n & 1) ? (n+1) / 2 : n / 2;
  if (n & 1) {
    memo[n] = fib(k)*fib(k) + fib(k-1)*fib(k-1);
  }
  else {
    memo[n] = (2*fib(k-1) + fib(k)) * fib(k);
  }
  return memo[n];
}

int main() {
  memo[0] = 0;
  memo[1] = 1;

  long long n;
  int i = 0;
  while (true) {
    long long x = fib(i++);
    // print until overflow - overflows at 93rd fib number
    if (x < 0) break;
    printf("%i\t\t%lld\n", i-1, x);
  }
  return 0;
}
