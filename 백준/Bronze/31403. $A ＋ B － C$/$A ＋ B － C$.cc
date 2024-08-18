#include <iostream>
#include <string>

using namespace std;

int main() {
    string A;
    string B;
    string C;
    string D;

    cin >> A >> B >> C;
    D = A+B;

    int a = stoi(A);
    int b = stoi(B);
    int c = stoi(C);
    int d = stoi(D);
    
    cout << a+b-c << endl << d-c;
    
    return 0;
}