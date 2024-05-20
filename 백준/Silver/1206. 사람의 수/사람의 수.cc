#include <iostream>
#include <vector>
#include <set>
#include <cmath>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> averages(N);
    for (int i = 0; i < N; ++i) {
        double avg;
        cin >> avg;
        averages[i] = static_cast<int>(round(avg * 1000));
    }

    int res = 1001;
    for (int p = 1; p <= 1000; ++p) {
        bool valid = true;
        set<int> possible_averages;

        for (int sum = 0; sum <= p * 10; ++sum) {
            int truncated_average = (sum * 1000) / p;
            possible_averages.insert(truncated_average);
        }

        for (const int &avg : averages) {
            if (possible_averages.find(avg) == possible_averages.end()) {
                valid = false;
                break;
            }
        }

        if (valid) {
            res = p;
            break;
        }
    }

    cout << res << endl;
    return 0;
}


