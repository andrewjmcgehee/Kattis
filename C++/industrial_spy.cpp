#include <algorithm>
#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#define MAX 10000000
using namespace std;

int main() {
    // boolean where index i indicates if i is prime
    vector<bool> is_prime(MAX, true);
    is_prime[0] = false;
    is_prime[1] = false;

    // sieve of eratosthenes to calculate primes
    for (int i = 2; i*i <= MAX; i++) {
        if (is_prime[i]) {
            for (int j = i*i; j <= MAX; j += i) {
                is_prime[j] = false;
            }
        }
    }

    int num_cases;
    cin >> num_cases;

    for (int i = 0; i < num_cases; i++) {
        string s;
        string sub;

        cin >> s;
        // sorted version of string is guaranteed smallest permutation
        sort(s.begin(), s.end());

        set<int> primes;
        int len = s.size();
        do {
            for (int j = 1; j <= len; j++) {
                // we must permute the power set of the string (excluding the null set)
                sub = s.substr(0, j);
                stringstream ss;

                // hack to convert type
                long n;
                ss << sub;
                ss >> n;

                if (is_prime[n]) {
                    primes.insert(n);
                }
            }
        } while (next_permutation(s.begin(), s.end()));

        // calculating the next permutation is often faster than calculating
        // all permutations. this method could be implemented on your own, in
        // a technical interview but std library is fine for now.
        cout << primes.size() << '\n';
    }
    return 0;
}
