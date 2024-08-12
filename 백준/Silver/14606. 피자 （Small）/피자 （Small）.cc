#include <iostream>
#include <vector>
using namespace std;

int solve(int n, vector<int>& dp) {
    if (n <= 1) {
        return 0;
    }

    int a = n / 2;
    int b = n - a;
    
    int result = a * b + solve(a, dp) + solve(b, dp);

    return result;
}

int main() {
    int N;
    cin >> N;

    vector<int> dp(101, 0); 

    cout << solve(N, dp) << endl;

    return 0;
}
