/*
Rating: ~ 2.8 / 10
Link: https://open.kattis.com/problems/kutevi
Complexity: O(n) where n is number of angles
Memory: O(1)
*/

#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int num_angles;
    int num_tests;
    cin >> num_angles;
    cin >> num_tests;

    // find greatest common divisor of all angles
    int gcd = 360;
    for (int i = 0; i < num_angles; i++) {
        int angle;
        cin >> angle;
        gcd = __gcd(gcd, angle);
    }

    // if test angle is divisble by gcd of all angles, it can be created
    for (int i = 0; i < num_tests; i++) {
        int test;
        cin >> test;
        if (test % gcd == 0) {
            cout << "YES" << '\n';
        }
        else {
            cout << "NO" << "\n";
        }
    }
}
