/*
Rating: ~ 1.8 / 10
Link: https://open.kattis.com/problems/mosquito
Complexity: O(n) where n is number of generations
Memory: O(1)
*/

#include <iostream>

using namespace std;

// lots of variables but just simple math
int main() {
    int M, P, L, E, R, S, N;
    while (cin >> M >> P >> L >> E >> R >> S >> N) {
        for (int i = 0; i < N; i++) {
            int newEggs = M * E;
            M = 0;
            M += P / S;
            P = 0;
            P += L / R;
            L = 0;
            L += newEggs;
        }
        cout << M << '\n';
    }
    return 0;

}
