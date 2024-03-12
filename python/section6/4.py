import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def DFS(L, sum):
  global cnt
  if L == k:
    if sum == T:
      cnt += 1
  else:
    for i in range(cn[L] + 1):
        DFS(L + 1, sum + cv[L] * i)

if __name__=="__main__":
  T = int(input())
  k = int(input())
  cv = []
  cn = []
  cnt = 0
  for i in range(k):
    p, n = map(int, input().split())
    cv.append(p)
    cn.append(n)
  
  DFS(0, 0)
  print(cnt)