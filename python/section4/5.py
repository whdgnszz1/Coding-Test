import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

# n, k = map(int, input().split())
# a = list(range(1, n + 1))
# a = deque(a)

# while len(a) > 1:
#   for i in range(k - 1):
#     a.append(a.popleft()) 
#   a.popleft()

# print(a[0])

n, k = map(int, input().split())
dq = list(range(1, n + 1))
dq = deque(dq)

while dq:
  for _ in range(k - 1):
    cur = dq.popleft()
    dq.append(cur)
  dq.popleft()
  if(len(dq) == 1):
    print(dq[0])
    dq.popleft()