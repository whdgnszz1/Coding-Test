#include<bits/stdc++.h>
using namespace std;
int a[9];
int main () {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  
  for (int i = 0; i < 9; i++) {
    cin >> a[i];
  }
  sort(a, a + 9);

  do {
    for (int i : a) cout << i << " ";
    cout << '\n';
    int sum = 0;
    for (int i = 0; i < 7; i++) sum += a[i];

    if (sum == 100) break;
  } while(next_permutation(a, a+9));

  for (int i = 0; i < 7; i++) cout << a[i] << "\n";
  return 0;
}