/*
Rating: ~ 1.6 / 10
Link: https://open.kattis.com/problems/server
Complexity:
*/

#include <iostream>

using namespace std;

int main() {
    int numbers;
    int minutes;
    cin >> numbers;
    cin >> minutes;

    // stop when tasks cause number to go over
    int tasks = 0;
    int sum = 0;
    for (int i = 0; i < numbers; i++) {
        int current;
        cin >> current;
        if (sum + current <= minutes) {
            sum += current;
            tasks++;
        }
        else {
            break;
        }
    }
    cout << tasks << '\n';
    return 0;
}
