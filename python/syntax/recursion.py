import sys
sys.stdin = open("input.txt", "rt")

def DFS(x):
  if x > 0:
    DFS(x - 1)
    print(x)

if __name__=="__main__":
  n = int(input())
  DFS(n)