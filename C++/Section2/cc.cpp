// 1번. 정점은 0번부터 9번까지 10개의 노드가 있다. 1 - 2 / 1 - 3 / 3 - 4 의 경로가 있을 때 이를 인접 행렬로 표현한다면?
// 2번. 0번부터 방문 안한 노드를 찾고 해당 노드부터 방문, 연결된 노드를 이어서 방문하여 출력하는 재귀함수를 만들고 싶다면 어떻게 해야할까?
// 또한, 정점을 방문하고 다시 방문하지 않게 만들으려면 어떻게 해야할까?

#include<bits/stdc++.h>
using namespace std;
const int V = 10;
bool a[V][V], visited[V];

void go(int from) {
  visited[from] = 1;
  cout << from << "\n";
  for(int i = 0; i < V; i++) {
    if(visited[i]) continue;
    if(a[from][i]) {
      go(i);
    }
  }
}

int main() {
  a[1][2] = 1; a[1][3] = 1; a[3][4] = 1;
  a[2][1] = 1; a[3][1] = 1; a[4][3] = 1;
  for(int i = 0; i < V; i++) {
    for(int j = 0; j < V; j++) {
      if(a[i][j] && visited[i] == 0) {
        go(i);
      }
    }
  }
}