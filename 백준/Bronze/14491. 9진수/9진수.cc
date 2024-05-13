# include <iostream>

using namespace std;

int main()
{
  int T;
  cin >> T;

  // 9 진법
  int N = T;
  int result = 0;
  int place = 1;
  
  while (N > 0){
    int left = N % 9;
    result += left * place;
    N /= 9;
    place *= 10;
  }
  cout << result << endl;

  return 0;
}