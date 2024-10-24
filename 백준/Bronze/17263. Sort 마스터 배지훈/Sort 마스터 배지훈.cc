#include <iostream>

using namespace std;

int main() {
    int N;
    int maxV = 0;
    int v;
    cin >> N;
    for (int i=0;i<N ; i++) {
        cin >> v;
        if (v > maxV) {
            maxV = v;
        }
    }

    cout << maxV << endl;
    return 0;
}