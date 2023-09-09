import sys
sys.stdin = open('input.txt')


def teach_u(start, cnt):
    if cnt == K - 5:
        check_num = 0
        for word in words:
            for w in word:
                if not words_list[ord(w) - ord('a')]:
                    break
            else:
                check_num += 1
        global ans
        if check_num > ans:
            ans = check_num

        return

    for num in range(start, 26):
        if not words_list[num]:
            words_list[num] = 1
            teach_u(num + 1, cnt + 1)
            words_list[num] = 0



N, K = map(int, input().split())
words = [set(input()) for _ in range(N)]
# print(words)
words_list = [0] * 26
first_words = list('antic')
# print(first_words)
for char in first_words:
    words_list[ord(char) - ord('a')] = 1
ans = 0
if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    teach_u(0, 0)
    print(ans)
# print(words_list)
