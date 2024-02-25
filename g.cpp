#include<bits/stdc++.h>
using namespace std;
// Array to decay는 vector타입은 안되고, 정적 배열만 가능하다.
int a[3] = {1, 2, 3};
int main() {
  // string a = "kundol";
  // string *b = &a;
  // cout << b << '\n';
  // cout << *b << '\n';
  // return 0;
  int * c = a;
  cout << c << "\n";
  cout << &a[0] << "\n";
  cout << c + 1 << "\n";
  cout << &a[1] << "\n";
  return 0;
}