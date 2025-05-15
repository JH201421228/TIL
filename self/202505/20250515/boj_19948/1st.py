import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


S = input().rstrip()
spacebar = int(input())
alphabet = list(map(int, input().split()))

title = ''

S = list(S.split())

if len(S)-1 > spacebar:
    print(-1)
    exit(0)

for s in S:
    c = s[0]

    if ord(c) > 96: title += chr(ord(c)-32)
    else: title += c

    for idx in range(len(s)):
        if idx and s[idx] == s[idx-1]: continue
        else:
            if ord(s[idx]) > 96: n = ord(s[idx])-97
            else: n = ord(s[idx])-65

        if alphabet[n]: alphabet[n] -= 1
        else:
            print(-1)
            exit(0)

for idx in range(len(title)):
    if idx and title[idx] == title[idx-1]: continue

    c = title[idx]

    if alphabet[ord(c)-65]: alphabet[ord(c)-65] -= 1
    else:
        print(-1)
        exit(0)

print(title)