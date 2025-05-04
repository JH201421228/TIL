import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


class number_attr:
    def __init__(self):
        self.cur = 0
        self.blank = 0
        self.num = []
        self.blanks = []

    def __str__(self):
        return f"{self.cur}, {self.blank}, {self.num}, {self.blanks}"


N, K = map(int, input().split())
arr = list(map(int, input().split()))

attr_dict = {}
pre = arr[0]
acc = 1
cur = arr[0]

for n in arr:
    attr_dict[n] = attr_dict.get(n, number_attr())

for idx in range(1, N):
    cur = arr[idx]

    if pre != cur:
        attr_dict[pre].num.append(acc)
        acc = 1
        if attr_dict[cur].num:
            attr_dict[cur].blanks.append(attr_dict[cur].blank)
        attr_dict[cur].blank = 0
    else:
        acc += 1

    for k, v in attr_dict.items():
        if k != cur:
            attr_dict[k].blank += 1

    pre = cur

attr_dict[cur].num.append(acc)

ans = 0
for k, v in attr_dict.items():
    res = v.num[0]
    pre_idx = 0
    cur_k = 0

    ans = max(ans, res)

    for idx in range(len(v.blanks)):
        cur_k += v.blanks[idx]
        res += v.num[idx + 1]
        if cur_k > K:
            while cur_k > K:
                cur_k -= v.blanks[pre_idx]
                res -= v.num[pre_idx]
                pre_idx += 1

        ans = max(ans, res)

print(ans)