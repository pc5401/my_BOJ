#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    unsigned long long n;
    cin >> n;
    if ((n & (n - 1)) == 0) {
        cout << "TAK\n";
    } else {
        cout << "NIE\n";
    }

    return 0;
}
