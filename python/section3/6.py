import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
player = []

for _ in range(n):
  t, w = map(int, input().split())
  player.append((t, w))
player.sort(reverse = True)

largest = 0
cnt = 0
for x, y in player:
  if y > largest:
    largest = y
    cnt += 1

print(cnt)