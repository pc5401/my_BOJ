#include <iostream>
#include <iomanip>  // for std::setw and std::setfill

using namespace std;

const long long MOD = 1e12;

int main()
{
  long long int N;
  cin >> N;

  long long int result = 1;
  for(long long int i = N; i > 0 ; i--)
  {
    result *= i;
    
    // 불필요한 큰 숫자의 곱셈 방지
    while (result % 10 == 0)  // 결과 값이 0으로 끝나면 불필요한 0 제거
      result /= 10;
    
    result %= MOD;
  }
   result %= 100000;

  // std::setw(5)를 사용해 항상 5자리 숫자로 출력하며, 부족한 자리는 0으로 채움
  cout << setw(5) << setfill('0') << result << endl;

  return 0;
}