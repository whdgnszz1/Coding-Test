import sys
sys.stdin = open("input.txt", "rt")

# a = input()
# stack = []

# for x in a:
#   if x.isdecimal():
#     stack.append(int(x))
#   elif x == '*':
#     cnt = stack.pop() * stack.pop()
#     stack.append(cnt)
#   elif x == '/':
#     a = stack.pop()
#     b = stack.pop()
#     cnt = b / a
#     stack.append(cnt)
#   elif x == '+':
#     cnt = stack.pop() + stack.pop()
#     stack.append(cnt)
#   elif x == '-':
#     cnt = - (stack.pop() - stack.pop())
#     stack.append(cnt)

# print(int(stack[0]))  

a = input()
stack = []

for x in a:
  if x.isdecimal():
    stack.append(int(x))
  else:
    if x == '+':
      n1 = stack.pop()
      n2 = stack.pop()
      stack.append(n2 + n1)
    elif x == '-':
      n1 = stack.pop()
      n2 = stack.pop()
      stack.append(n2 - n1)
    elif x == '*':
      n1 = stack.pop()
      n2 = stack.pop()
      stack.append(n2 * n1)
    elif x == '/':
      n1 = stack.pop()
      n2 = stack.pop()
      stack.append(n2 / n1)

print(stack[0])            