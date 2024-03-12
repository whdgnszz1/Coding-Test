import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# def DFS(L, sumA, sumB, sumC):
#   global res
#   if L == n:
#     if sumA != sumB and sumB != sumC and sumA != sumC:
#       arr = [sumA, sumB, sumC]
#       arr.sort()
#       res.add(arr[-1] - arr[0])
#   else:
#     DFS(L + 1, sumA + a[L], sumB, sumC)
#     DFS(L + 1, sumA, sumB + a[L], sumC)
#     DFS(L + 1, sumA, sumB , sumC + a[L])

# if __name__=="__main__":
#   n = int(input())
#   a = list()
#   for i in range(n):
#     c = int(input())
#     a.append(c)
#   s = sum(a)
#   ch = list()
#   res = set()
#   DFS(0, 0, 0, 0)
#   print(min(res))

def DFS(L):
  global res
  if L == n:
    cha = max(money) - min(money)
    if cha < res:
      tmp = set()
      for x in money:
        tmp.add(x)
      if len(tmp) == 3:
        res = cha
  else:
    for i in range(3):
      money[i] += coin[L]
      DFS(L + 1)
      money[i] -= coin[L]

if __name__=="__main__":
  n = int(input())
  coin = list()
  money = [0] * 3
  res = 2147483647
  for _ in range(n):
    coin.append(int(input()))
  DFS(0)
  print(res)