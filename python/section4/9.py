import sys
sys.stdin = open("input.txt", "rt")

s1 = input()
s1Dict = dict()
s2 = input()
s2Dict = dict()

for x in s1:
  s1Dict[x] = s1Dict.get(x, 0) + 1

for x in s2:
  s2Dict[x] = s2Dict.get(x, 0) + 1

for i in s1Dict.keys():
  if i in s2Dict.keys():
    if s1Dict[i] != s2Dict[i]:
      print("NO")
      break
  else:
    print("NO")
    break
else:
  print("YES")    