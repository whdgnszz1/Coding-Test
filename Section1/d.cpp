#include <bits/stdc++.h>
using namespace std;

// 4개 이상 뽑을땐 재귀함수, 이하는 중첩for문
int n = 5, k = 3, a[5] = {1, 2, 3, 4, 5};
void print(vector<int> b) {
  for (int i : b) cout << i << " ";
  cout << '\n';
}

// 외우기!
void combi(int start, vector<int> b) {
  if(b.size() == k ) {
    print(b);
    return;
  }
  for(int i = start + 1 ; i < n ; i++) {
    b.push_back(i);
    combi(i, b);
    b.pop_back();
  }
}

int main () {
  vector<int> b;
  // combi(-1, b);
  for (int i = 0; i < n; i++) {
    for(int j = 0; j < i; j++) {
      for(int k = 0; k < j; k++) {
        cout << i << " : " << j << " : " << k << '\n';
      }
    }
  }
  return 0;
}