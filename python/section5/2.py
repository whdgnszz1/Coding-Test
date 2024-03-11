import sys
sys.stdin = open("input.txt", "r")

# 대부분 전위 순회를 사용하지만, 병합 정렬의 경우 후위 순회를 사용한다.
def DFS(v):
  if v > 7:
    return
  else:
    DFS(v * 2)
    DFS(v * 2 + 1)
    print(v)

if __name__=="__main__":
  DFS(1)