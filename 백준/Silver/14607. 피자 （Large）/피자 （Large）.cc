#include <iostream>
#include <vector>
using namespace std;

long solve(long n, vector<long>& dp) {
    if (n <= 1) {
        return 0;
    }

    if (n < dp.size() && dp[n] != -1) {
        return dp[n];
    }

    long a = n / 2;
    long b = n - a;
    
    long result = a * b + solve(a, dp) + solve(b, dp);

    if (n < dp.size()) {
        dp[n] = result;
    }

    return result;
}

int main() {
    long N;
    cin >> N;

    vector<long> dp(1001, -1);  // 메모이제이션을 위한 크기 101의 배열 (-1로 초기화)

    cout << solve(N, dp) << endl;

    return 0;
}
