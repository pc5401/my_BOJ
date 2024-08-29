#include <iostream>
using namespace std;

double integral(int x, int a, int b, int c, int d, int e) {
    return (a / 3.0) * x * x * x + (b - d) / 2.0 * x * x + (c - e) * x;
}

int main() {
    // 입력값
    int x1, x2;
    cin >> x1 >> x2;

    int a, b, c, d, e;
    cin >> a >> b >> c >> d >> e;

    // 풀이
    double result = integral(x2, a, b, c, d, e) - integral(x1, a, b, c, d, e);

    // 출력
    cout << static_cast<int>(result) << endl;

    return 0;
}
