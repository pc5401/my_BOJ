#include <iostream>
#include <queue>
#include <string>

using namespace std;

int main() {
    queue<int> Q;
    
    int N;
    cin >> N;
    
    string order;
    for (int i = 0; i < N; i++) {
        cin >> order;
        if (order == "push") {
            int x;
            cin >> x;
            Q.push(x);
        } else if (order == "pop") {
            if (Q.empty()) {
                cout << -1 << endl;
            } else {
                cout << Q.front() << endl;
                Q.pop();
            }
        } else if (order == "size") {
            cout << Q.size() << endl;
        } else if (order == "empty") {
            cout << (Q.empty() ? 1 : 0) << endl;
        } else if (order == "front") {
            if (Q.empty()) {
                cout << -1 << endl;
            } else {
                cout << Q.front() << endl;
            }
        } else if (order == "back") {
            if (Q.empty()) {
                cout << -1 << endl;
            } else {
                cout << Q.back() << endl;
            }
        }
    }

    return 0;
}
