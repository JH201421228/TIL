

check_num = int(input())
ans = check_num

for _ in range(check_num):
    words = str(input())

    for i in range(len(words) - 1):
        if words[i] == words[i + 1]:
            pass
        elif words[i] in words[i + 1:]:
            ans -= 1
            break

print(ans)