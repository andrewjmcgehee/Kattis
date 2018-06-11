#include <iostream>

using namespace std;

int main() {
    int a, b, range;
    cin >> a >> b >> range;

    for (int i = 1; i <= range; i++) {
        // must check if it meets both conditions first
        if (i % b == 0 && i % a == 0) {
            cout << "FizzBuzz\n";
        }
        else if (i % a == 0) {
            cout << "Fizz\n";
        }
        else if (i % b == 0) {
            cout << "Buzz\n";
        }
        else {
            cout << i << '\n';
        }
    }
}
