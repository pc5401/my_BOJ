#include <iostream>
#include <vector>
using namespace std;

int solve(int n, int m, int k) {
    vector<int> callers(n);
    for (int i = 0; i < n; i++) {
        callers[i] = i + 1;
    }
    int cur = 0;
    for (int i = 0; i < k - 1; i++) {
        cur = (cur + m - 1) % callers.size();
        callers.erase(callers.begin() + cur);
    }
    cur = (cur + m - 1) % callers.size();
    return callers[cur];
}

int main() {
    int n, m, k;
    while (cin >> n >> m >> k) {
        if (n == 0 && m == 0 && k == 0) break;
        cout << solve(n, m, k) << "\n";
    }
    return 0;
}
