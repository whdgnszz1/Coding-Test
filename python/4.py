import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
avg = round(sum(a) / n)
min = float('inf')

for idx, x in enumerate(a):
  tmp = abs(x - avg)
  if tmp < min:
    min = tmp
    score = x
    res = idx + 1
  elif tmp == min:
    if(x > score):
      score = x
      res = idx + 1

print(avg, res)