word = str(input())
cursor = len(word)
for i in range(int(input())):
    input_keys = list(map(str, input().split()))

    if input_keys[0] == 'L':
        if cursor != 0:
            cursor -= 1
    
    elif input_keys[0] == 'D':
        if cursor != len(word):
            cursor += 1

    elif input_keys[0] == 'B':
        if cursor != 0:
            word = word[:cursor - 1] + word[cursor:]
            cursor -= 1

    else:
        word = word[:cursor] + input_keys[1] + word[cursor:]
        cursor += 1

print(word)