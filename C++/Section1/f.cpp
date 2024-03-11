#include<bits/stdc++.h>
using namespace std;
// int i;

// int main() {
//   cout << &i << '\n';
//   i = 0;
//   cout << &i << '\n';
// }

double a = 4.4;
int c = 10;
int main() {
  // <타입> * <변수명> = <해당 타입의 변수의 주소>
  // * 은 에스터리스크 라고 함!
  // 포인터의 크기는 os체제의 비트마다 다르다. 32비트는 무조건 4byte, 64비트는 무조건 8byte
  cout << &a << '\n';
  double *b = &a;
  int *d = &c;
  cout << sizeof(b) << '\n';
  cout << sizeof(d) << '\n';
}