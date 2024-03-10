import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
b = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    row, dir, cnt = b[i]
    # 왼쪽으로 회전
    if dir == 0:
        for _ in range(cnt):
            a[row - 1].append(a[row - 1].pop(0))
    # 오른쪽으로 회전
    else:
        for _ in range(cnt):
            a[row - 1].insert(0, a[row - 1].pop())

e = n
s = 0
res = 0
for i in range(n):
  for j in range(s, e):
    res += a[i][j]
  if i < n // 2:
    s += 1
    e -= 1
  else:
    s -= 1
    e += 1

print(res)