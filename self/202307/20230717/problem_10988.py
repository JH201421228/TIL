

check_word = str(input())

check_num = 0

for i in range(len(check_word)):
    if check_word[i] == check_word[-(i + 1)]:
        check_num = 1
    else:
        check_num = 0
        break
    
print(check_num)