import sys
sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split(" "))
cnt = 0

# def isPrime(x):
#     if x < 2: 
#         return False
#     for i in range(2, int(x**0.5) + 1):  
#         if x % i == 0:  
#             return False
#     return True  

for i in range (1, n + 1):
  if n % i == 0:
    cnt += 1
  if cnt == k:
    print(i)
    break
else:
  print(-1)