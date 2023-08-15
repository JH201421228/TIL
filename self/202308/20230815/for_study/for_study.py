def why_do_this(K, ans):
    if len(ans) == K:
        print(ans)
        return

    for i in range(0, K):
        ans.append(arr[i])
        why_do_this(K, ans)
        ans.pop()

N, K = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
why_do_this(K, ans)