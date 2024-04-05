#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 2;
    for (int x = 2; x <= n; x++){
        if (n % x == 1) return x;
    }
    return answer;
}