import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

S = list(input().rstrip())
S_dict = {}

for s in S:
    S_dict[s] = S_dict.get(s, 0) + 1

cnt = 0
even, odd = [], []
for k, v in S_dict.items():
    if v % 2:
        cnt += 1
        odd.append(k)
        if cnt > 1:
            print("I'm Sorry Hansoo")
            exit(0)
        if v > 1:
            even.append(k)
            S_dict[k] -= 1

    else:
        even.append(k)

even.sort()
ans = []

for c in even:
    n = S_dict[c] // 2
    for _ in range(n):
        ans.append(c)

reverse_ans = [*ans]
reverse_ans.sort(reverse=True)

ans.extend(odd)
ans.extend(reverse_ans)

print(''.join(ans))