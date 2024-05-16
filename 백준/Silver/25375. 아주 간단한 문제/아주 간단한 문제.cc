#include <iostream>
#include <vector>

using namespace std;

bool solve(long long a, long long b) {
    if (b % a != 0) return false;
    long long m = b / a;
    return m >= 2;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int Q;
    cin >> Q;
    
    vector<bool> results(Q); // 결과 저장을 위한 벡터

    for (int i = 0; i < Q; ++i) {
        long long a, b;
        cin >> a >> b;
        results[i] = solve(a, b);
    }

    // 결과를 한 번에 출력
    for (int i = 0; i < Q; ++i) {
        cout << (results[i] ? 1 : 0) << '\n';
    }

    return 0;
}