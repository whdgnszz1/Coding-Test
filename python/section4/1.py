import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
num = list(map(int, str(n)))
stack = []

# for x in num:
#     # 스택이 비어있지 않고, m이 0보다 크며, 스택의 마지막 값이 현재 값보다 작은 경우
#     # 스택의 마지막 값을 제거
#     while stack and m > 0 and stack[-1] < x:
#         stack.pop()
#         m -= 1
#     stack.append(x)

# # m이 여전히 남아있는 경우(즉, 제거할 숫자가 남았다면) 스택의 뒤에서부터 제거
# res = stack[:-m] if m > 0 else stack

# print(''.join(res))

for x in num:
  while stack and m > 0 and stack[-1] < x:
    stack.pop()
    m -= 1
  stack.append(x)

if m != 0:
  stack = stack[:-m]

res = ''.join(map(str, stack))
print(res)