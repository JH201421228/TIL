# 2 + 3 * 4 / 5

cal = '2+3*4/5'
result = ''
stack = []
for char in cal:
    if char not in '+-*/':
        result += char
    else:
        stack.append(char)
while stack:
    result += stack.pop()
print(result, stack)
