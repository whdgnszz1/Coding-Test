msg = "It is Time"
print(msg.upper())
print(msg.lower())
print(msg)
tmp = msg.upper()
print(tmp.find("T"))
print(tmp.count("T"))
print(msg[:2])
print(msg[3:5])
print(len(msg))

for x in msg:
  if x.isupper():
    print(x, end = " ")
print()

for x in msg:
  if x.islower():
    print(x, end = " ")
print()

for x in msg:
  if x.isalpha():
    print(x, end = "")
print()

tmp = 'AZ'
for x in tmp:
  print(ord(x))


tmp = 'az'
for x in tmp:
  print(ord(x))

tmp = 65
print(chr(tmp))