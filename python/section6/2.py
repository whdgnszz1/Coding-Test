import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# def DFS(L, sum):
#   global res
#   if L >= 7:
#     if sum > res:
#       res = sum
#   else:
#     DFS(L + ti[L], sum + pi[L])
#     DFS(L + 1, sum)

# if __name__=="__main__":
#   n = int(input())
#   ti = list()
#   pi = list()
#   for i in range(n):
#     a, b = map(int, input().split())
#     ti.append(a)
#     pi.append(b)
#   res = -2147483647
#   DFS(0, 0)
#   print(res)

def DFS(L, sum):
  global res
  if L == n + 1:
    if sum > res:
      res = sum
  else:
    if L + T[L] <= n + 1:
      DFS(L + T[L], sum + P[L])
    DFS(L + 1, sum)

if __name__=="__main__":
  n = int(input())
  T = list()
  P = list()
  for i in range(n):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)
  res = -2147483647
  T.insert(0, 0)
  P.insert(0, 0)
  DFS(1, 0)
  print(res)