import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
words_length = 0
words = [input().rstrip() for _ in range(N)]

for word in words:
    words_length += len(word)

interval = M - words_length

share_n = interval // (N-1)
remainder_n = interval % (N-1)

if not remainder_n:
    print(('_' * share_n).join(words))
    exit(0)

ans = ('_' * share_n).join(words)
temp_len = len(ans)

cur = 0
for idx in range(temp_len-1):
    if ans[idx+cur] == '_' and ord(ans[idx+cur+1]) > 96:
        ans = ans[:idx+cur] + '_' + ans[idx+cur:]
        remainder_n -= 1
        cur += 1

    if not remainder_n:
        break
else:
    temp_len = len(ans)
    for idx in range(temp_len-1, 1, -1):
        if ans[idx-1] == '_' and ord(ans[idx]) < 91:
            ans = ans[:idx] + '_' + ans[idx:]
            remainder_n -= 1

        if not remainder_n:
            break

print(ans)