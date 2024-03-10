import sys
sys.stdin = open("input.txt", "rt")

l = int(input())
init = list(map(int, input().split()))
m = int(input())
init.sort()

for _ in range(m):
  init[0] = init[0] + 1
  init[l - 1] = init[l - 1] - 1
  init.sort()
  
print(init[l - 1] - init[0])