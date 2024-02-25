#include<bits/stdc++.h>
using namespace std;
vector<int> v;
void printV(vector<int> $v) {
  for (int i = 0; i < v.size(); i++) {
    cout << v[i] << " ";
  }
  cout << "\n";
}

void makePermutation (int n, int r, int depth) {
  cout << n << " : " << r << " : " << depth << "\n";
  if (r == depth) {
    printV(v);
    return;
  }
  for (int i = depth; i < n; i++) {
    // swap: 원복
    swap(v[i], v[depth]);
    makePermutation(n, r, depth + 1);
    swap(v[i], v[depth]);
  }
  return;
}

// 재귀함수 외우기!
void f (int n, int r, int depth ) {
  if(r == depth) {
    //logic
    return;
  }
  for(int i = depth; i  < n ; i++) {
    swap(v[i], v[depth]);
    f(n, r, depth + 1);
    swap(v[i], v[depth]);
  }
}

int main () {
  for (int i = 1; i <= 3; i++) v.push_back(i);
  makePermutation(3, 3, 0);
  return 0;
}