s = input()
result = []


for i in range(len(s)):
  if s[i] == ' ':
    result.append("%20")
  else:
    result.append(s[i])

print(''.join(result))