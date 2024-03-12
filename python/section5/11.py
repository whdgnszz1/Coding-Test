import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# def DFS(L, start, sum):
#   global cnt
#   if L == k:
#     if sum % m == 0:
#       cnt += 1
#   else:
#     for i in range(start, n + 1):
#       p[L] = i
#       DFS(L + 1, i + 1, sum + a[i - 1])


# if __name__=="__main__":
#   n, k = map(int, input().split())
#   a = list(map(int, input().split()))
#   m = int(input())
#   p = [0] * k
#   cnt = 0
#   DFS(0, 1, 0)
#   print(cnt)

def DFS(L, s, sum):
  global cnt
  if L == k:
    if sum % m == 0:
      cnt +=1
  else:
    for i in range(s, n):
      DFS(L + 1, i + 1, sum + a[i])

if __name__=="__main__":
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  m = int(input())
  cnt = 0
  DFS(0, 0, 0)

print(cnt)