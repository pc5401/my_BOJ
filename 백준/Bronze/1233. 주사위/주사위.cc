#include <iostream>
#include <vector>

using namespace std;

int main() {
    int S1, S2, S3;
    cin >> S1 >> S2 >> S3;

    vector<int> arr(100, 0);

    for (int i = 1; i <= S1; i++) {
        for (int j = 1; j <= S2; j++) {
            for (int k = 1; k <= S3; k++) {
                arr[i+j+k]++;
            }
        }
    }

    int result = 0;

    for (int i = 0; i <= 100; i++){
        if (arr[i] > arr[result]) result = i;
    }
    
    cout << result << endl;
    return 0;
}