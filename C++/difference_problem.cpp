#include <iostream>
#include <cmath>

using namespace std;

int main() {
    long long a, b;
    while (cin >> a >> b) {
        long long diff = abs(a - b);
        cout << diff << '\n';
    }
}
