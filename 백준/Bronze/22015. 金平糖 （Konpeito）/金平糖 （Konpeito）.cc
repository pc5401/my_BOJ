#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solve(vector<int>& data) {
    int m = *max_element(data.begin(), data.end());
    int rtn = 0;
    for (int d : data) {
        rtn += (m - d);
    }
    return rtn;
}

int main() {
    // 입력값
    vector<int> data(3);
    for (int i = 0; i < 3; ++i) {
        cin >> data[i];
    }
    
    // 풀이
    int result = solve(data);
    
    // 출력
    cout << result << endl;
    
    return 0;
}

