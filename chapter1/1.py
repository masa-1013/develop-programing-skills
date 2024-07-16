s = input()

l = [False] * 128

for i in range(len(s)):
  if (len(s) > 128):
    print("NG")
    exit()
  
  if l[ord(s[i])]:
    print("NG")
    exit()
  
  l[ord(s[i])] = True

    
print("OK")