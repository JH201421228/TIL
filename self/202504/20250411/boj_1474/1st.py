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

ans = ('-' * share_n).join(words)
temp_len = len(ans)

for idx in range(temp_len, 0, -1):
    pass

print(ans)

print(words_length)
print(share_n, remainder_n)

print(ord('A'), ord('Z'), ord('a'), ord('z'))