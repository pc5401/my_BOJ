#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>

using namespace std;

void solve(int n, int start, int sub, int end){ // 하노이탑 출력
    if (n == 1) {
        printf("%d %d\n", start, end);
        return;
    }
     // n-1개의 원판을 보조 기둥으로 이동
    solve(n-1, start, end, sub);

     // 가장 큰 원판을 목적지로 이동
    printf("%d %d\n", start, end);

    // 보조 기둥에 있는 n-1개의 원판을 목적지로 이동
    solve(n-1, sub, start, end);
}

int main() {
    int N;
    cin >> N;

    // 구글링에서 찾은 하노이 탑 이동 횟수 계산
    string a = to_string(pow(2, N));

    int x = a.find('.');
    a = a.substr(0, x);
    a[a.length() - 1] -= 1; 

    cout << a << endl;

    if(N <= 20) {
        solve(N, 1, 2, 3);
    }

    return 0;
}
