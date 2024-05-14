#include <iostream>
#include <vector>
#include <sstream>
using namespace std;

int main() {
    int T;
    cin >> T;  // 테스트 케이스의 개수 입력 받음
    cin.ignore();  // 버퍼 비우기

    for (int i = 0; i < T; ++i) {
        string line;
        getline(cin, line);  // 한 줄 입력 받음

        stringstream ss(line);
        int number, sum = 0;

        // 한 줄에서 숫자를 하나씩 추출하여 더하기
        while (ss >> number) {
            sum += number;
        }

        cout << sum << endl;  // 합 출력
    }

    return 0;
}
