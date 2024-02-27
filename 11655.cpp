#include<bits/stdc++.h>
using namespace std;
string s;
int main () {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  
  getline(cin, s);
  for(int i = 0; i < s.size(); i++) {
    // 대문자인 경우
    if(s[i] >= 'A' && s[i] < 'a') {
      if(s[i] + 13 > 'Z') s[i] = s[i] + 13 - 26;
      else s[i] = s[i] + 13;
    } 
    // 소문자인 경우
    else if (s[i] >= 'a' && s[i] <= 'z') {
      if(s[i] + 13 > 'z') s[i] = s[i] + 13 - 26;
      else s[i] = s[i] + 13;
    }
    cout << s[i];
  }

  return 0;
}
