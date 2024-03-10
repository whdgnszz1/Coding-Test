# def add(a, b):
#   c = a + b
#   return c

# d = add(3, 2)
# print(d)

# def add(a, b):
#   c = a + b
#   d = a - b
#   return c, d

# x = add(3, 2)
# print(x)

def isPrime(x):
  for i in range (2, x):
    if (x % i == 0):
      return False
  return True  


a = [12, 13, 7, 9, 19]

for x in a:
  if(isPrime(x)):
    print(x)
  else:
    print(False)  