#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    vector<int> arr;
    int v;
    cin >> N;
    for (int i=0;i<N ; i++) {
        cin >> v;
        arr.push_back(v);
    }
    int result = *max_element(arr.begin(), arr.end());

    cout << result << endl;
    return 0;
}