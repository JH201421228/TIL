import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


for _ in range(int(input())):
    words = list(input().rstrip())

    l = len(words)

    idx = 0

    for i in range(1, l):
        if words[-i] > words[-i-1]:
           idx = i
           break
    else:
        print(''.join(words))
        continue

    target_idx = 0
    for i in range(l-idx, l):
        if words[i] > words[-idx-1]:
            target_idx = i

    words[-idx-1], words[target_idx] = words[target_idx], words[-idx-1]

    temp = sorted(words[l-idx:])
    ans = words[:l-idx] + temp

    print(''.join(ans))