

words_num = int(input())
cnt_num = words_num

for _ in range(words_num):
    words = str(input())
    
    for i in range(len(words) - 1):
        if words[i] == words[i + 1]:
            pass
        
        elif words[i] in words[i + 1:]:
            cnt_num -= 1
            break
        
print(cnt_num)