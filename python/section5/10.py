import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def DFS(L, start):
  if L == m:
    for x in p:
        print(x, end=" ")
    print()
    return
  else:
    for i in range(start, n + 1):
      p[L] = i
      DFS(L + 1, i + 1)

if __name__=="__main__":
  n, m = map(int, input().split())
  p = [0] * m 
  DFS(0, 1)
