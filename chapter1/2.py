a = input()
b = input()

if len(a) != len(b):
  print("NG")
  exit()

for i in range(len(a)):
  if a[i] != b[len(b) - (i + 1)]:
    print("NG")
    exit()

print("OK")