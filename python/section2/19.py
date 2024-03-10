import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0] * n)
a.append([0] * n)

dx = [-1, 0, 1, 0] 
dy = [0, 1, 0, -1]

for x in a:
  x.insert(0, 0)
  x.append(0)

cnt = 0
for i in range(n + 1):
  for j in range(n + 1):
    if all(a[i][j] > a[i + dx[k]][j + dy[k]] for k in range(4)):
      cnt += 1

print(cnt)
