#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solve(int n, vector<int> lst){
    int lo = 0;
    int hi = 1;
    int rtn = 0;
    int clockwise, counterclockwise;
    
    while (lo < hi){
        clockwise = lst[hi] - lst[lo];
        counterclockwise = (lst[n] - lst[hi]) + lst[lo];

        rtn = max(rtn, min(clockwise, counterclockwise));
        
        if (counterclockwise > clockwise) hi++;
        else lo++;

        if (hi >= n) break;
    }

    return rtn;
}

int main() {
    int n;
    cin >> n;

    vector<int> lst(n+1);
    lst[0] = 0;

    for (int i = 1; i <= n; i++){
        cin >> lst[i];
        lst[i] += lst[i-1];
    }


    int result = solve(n, lst);
    cout << result;
    
    return 0;
}