import sys
sys.stdin = open("input.txt", "r")

# def DFS(v):
#   if v == n + 1:
#     for i in range(1, n + 1):
#       if ch[i - 1] == 1:
#         a1.append(a[i - 1])
#       if ch[i - 1] == 0:
#         a2.append(a[i - 1])
#     if sum(a1) == sum(a2):
#       print("YES")
#     else:
#       print("NO")
#   else:
#     ch[v - 1] = 1
#     DFS(v + 1)
#     ch[v - 1] = 0
#     DFS(v + 1)

# if __name__=="__main__":
#   n = int(input())
#   a = list(map(int, input().split()))
#   ch = [0] * n
#   a1 = []
#   a2 = []
#   DFS(1)

def DFS(L, sum):
  if sum > total // 2:
    return
  if L == n:
    if sum == (total - sum):
      print("YES")
      sys.exit(0)
  else:
    DFS(L + 1, sum + a[L])
    DFS(L + 1, sum)

if __name__=="__main__":
  n = int(input())
  a = list(map(int, input().split()))
  total = sum(a)
  DFS(0, 0)
  print("NO")