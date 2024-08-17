#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    stack<int> Q;
    
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
                cout << Q.top() << endl;
                Q.pop();
            }
        } else if (order == "size") {
            cout << Q.size() << endl;
        } else if (order == "empty") {
            cout << (Q.empty()) << endl;
        } else if (order == "top") {
            if (Q.empty()) {
                cout << -1 << endl;
            } else {
                cout << Q.top() << endl;
            }
        }
    }

    return 0;
}
