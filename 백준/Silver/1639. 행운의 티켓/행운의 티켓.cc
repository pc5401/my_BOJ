#include <iostream>

using namespace std;

int solve(string s)
{
  int N = s.length();
  int result = 0;

  for (int n = 0; n < N; n++)
  {
    int left = 0, right = 0;
    int i = n, j = i+1;
    while (i >= 0 && j < N)
    {
      left += int(s[i]);
      right += int(s[j]);
      if (left == right && (j - i + 1) > result)
        result = j-i+1;
      i--;
      j++;
    }
  }
  return result;
}

int main()
{
  string s;
  cin >> s;

  int result = solve(s);
  cout << result << endl;

  return 0;
}
