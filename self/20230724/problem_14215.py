leng_list = list(map(int, input().split()))

if 2 * max(leng_list) >= sum(leng_list):
    ans = (sum(leng_list) - max(leng_list)) * 2 - 1
    print(ans)

else:
    print(sum(leng_list))
