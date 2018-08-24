/*
Rating: ~ 3.1 / 10
Link: https://open.kattis.com/problems/wheresmyinternet
Complexity: O(Log N) for union find with path compression
Memory: O(n) where n is number of disjoint elements
*/

#include <iostream>

using namespace std;

#define MAX 200001

int parent[MAX];

// union find functions
int find(int x) {
    return parent[x] == x ? x : parent[x] = find(parent[x]);
}

void unite(int x, int y) {
    parent[find(x)] = find(y);
}

int main() {
    for (int i = 0; i < MAX; i++) {
        parent[i] = i;
    }

    int n;
    int m;
    cin >> n >> m;

    // unite each pair
    for (int i = 0; i < m; i++) {
        int a;
        int b;
        cin >> a >> b;
        a--;
        b--;
        unite(a,b);
    }

    // check if connected by testing against root at 0
    bool connected = true;
    for (int i = 0; i < n; i++) {
        if (find(i) != find(0)) {
            cout << i+1 << endl;
            connected = false;
        }
    }

    if (connected) {
        cout << "Connected" << endl;
    }

    return 0;
}

