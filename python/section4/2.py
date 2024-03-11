import sys
sys.stdin = open("input.txt", "rt")

# split = str(input())
# stack = []
# cnt = 0

# for i in range(len(str(pipe))):
#   if i == 0 or len(stack) == 0:
#     stack.append(pipe[i])
#   else:
#     if stack[-1] == '(' and pipe[i] == ')' and pipe[i - 1] == '(':
#       stack.pop()
#       cnt += len(stack)
#     elif stack[-1] == '(' and pipe[i] == ')' and pipe[i - 1] == ')':
#       stack.pop()
#       cnt += 1
#     else:
#       stack.append(pipe[i])

# print(cnt)

s = input()
stack = []
cnt = 0

for i in range(len(s)):
  if s[i] == '(':
    stack.append(s[i])
  else:
    stack.pop()
    if s[i - 1] == '(':
      cnt += len(stack)
    else:
      cnt += 1

print(cnt)