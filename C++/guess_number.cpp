/*
Rating: ~ 3.2 / 10
Link: https://open.kattis.com/problems/guess
Complexity: O(Log N)
Memory: O(1)
*/

#include <iostream>
#include <string>

using namespace std;

int main() {
    bool found = false;

    string answer;
    int upper = 1001;
    int lower = 0;

    // with given info we know a binary search will work in enough tries
    while (!found) {
        // guess is always half the range of the upper and lower bound
        // (int divided)
        int guess = (upper + lower) / 2;
        cout << guess << '\n';
        cin >> answer;

        if (answer.compare("lower") == 0) {
            upper = guess;
        }
        else if (answer.compare("higher") == 0) {
            lower = guess;
        }
        else if (answer.compare("correct") == 0) {
            found = true;
        }
    }
    return 0;
}
