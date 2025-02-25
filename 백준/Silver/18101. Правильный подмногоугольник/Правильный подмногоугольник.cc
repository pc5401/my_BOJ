#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N;
    cin >> N;

    long long answer = N;

    long long limit = static_cast<long long>(floor(sqrtl(N)));

    for(long long d = 2; d <= limit; d++) {
        if(N % d == 0) {
            if(d >= 3) {
                answer = min(answer, d);
            }
            long long other = N / d;
            if(other >= 3) {
                answer = min(answer, other);
            }
        }
    }

    cout << answer << "\n";
    return 0;
}
