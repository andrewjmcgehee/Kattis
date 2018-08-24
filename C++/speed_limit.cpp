/*
Rating: ~ 1.4 / 10
Link: https://open.kattis.com/problems/speedlimit
Complexity: O(n) where n is number of entries
Memory: O(1)
*/

#include <iostream>

using namespace std;

int main() {
    int legs;
    cin >> legs;

    // basic math, just have to calculate elapsed time
    while (legs != -1) {
        int dist = 0;
        int time = 0;
        for (int i = 0; i < legs; i++) {
            int speed;
            int elapsed;
            cin >> speed >> elapsed;

            elapsed -= time;
            time += elapsed;
            dist += speed * elapsed;
        }
        cout << dist << " miles\n";
        cin >> legs;
    }
}
