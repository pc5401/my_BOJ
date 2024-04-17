#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

class BaseballSimulation {
private:
    int n;
    vector<vector<int>> play_data;
    int result;

public:
    BaseballSimulation(int N, vector<vector<int>> data) : n(N), play_data(data), result(0) {}

    int calculate_score(vector<int>& lineup) {
        int score = 0;
        int idx = 0;

        for (auto& inning : play_data) {
            deque<int> loo = {0, 0, 0};
            int out = 0;
            while (out < 3) {
                int player = lineup[idx % 9];
                if (inning[player] == 0) {
                    out += 1;
                } else {
                    loo.push_front(1);
                    score += loo.back();
                    loo.pop_back();
                    for (int i = 0; i < inning[player] - 1; ++i) {
                        loo.push_front(0);
                        score += loo.back();
                        loo.pop_back();
                    }
                }
                idx++;
            }
        }

        return score;
    }

    int simulate() {
        vector<int> lineup(9, 0);
        vector<int> players = {1, 2, 3, 4, 5, 6, 7, 8};

        do {
            for (int i = 0; i < 3; ++i) {
                lineup[i] = players[i];
            }
            for (int i = 3; i < 8; ++i) {
                lineup[i + 1] = players[i];
            }

            result = max(result, calculate_score(lineup));
        } while (next_permutation(players.begin(), players.end()));

        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<vector<int>> play_data(N, vector<int>(9));

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < 9; ++j) {
            cin >> play_data[i][j];
        }
    }

    BaseballSimulation simulation(N, play_data);
    cout << simulation.simulate() << "\n";

    return 0;
}
