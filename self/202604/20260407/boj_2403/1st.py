import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def available(i, j, l, dic):
    maxx, minx = -float("inf"), float("inf")
    cnt = 0
    for y, xs in dic.items():
        if y >= j and y <= j+l:
            if xs[-1] - xs[0] <= l and xs[0] >= i and xs[-1] <= i+l:
                maxx = max(maxx, xs[-1])
                minx = min(minx, xs[0])
                if maxx-minx > l: return False, cnt
                cnt += len(xs)
            else: return False, cnt
    
    return True, cnt


def solve():
    N = int(input())
    
    coordinate = [tuple(map(int, input().split())) for _ in range(N)]
    
    max_x, min_x = -float("inf"), float("inf")
    max_y, min_y = -float("inf"), float("inf")
    
    for x, y in coordinate:
        max_x = max(max_x, x)
        min_x = min(min_x, x)
        
        max_y = max(max_y, y)
        min_y = min(min_y, y)
        
        
    length = max(max_x-min_x, max_y-min_y)
    
    coordinate.sort(key=lambda x: x[1])
    
    
    dic = dict()
    for i, j in coordinate:
        if j in dic: dic[j].append(i)
        else: dic[j] = [i]
    
    s, e = 0, 60_000
    
    while s <= e:
        mid = (s+e)>>1
        
        a, a_cnt = available(min_x, min_y, mid, dic)
        b, b_cnt = available(max_x-mid, max_y-mid, mid, dic)
        
        if a and b and a_cnt + b_cnt >= N: e = mid-1
        else: s = mid+1
    tmp1 = s
        
    s, e = 0, 60_000
    
    while s <= e:
        mid = (s+e)>>1
        
        a, a_cnt = available(max_x-mid, min_y, mid, dic)
        b, b_cnt = available(min_x, max_y-mid, mid, dic)
        
        if a and b and a_cnt + b_cnt >= N: e = mid-1
        else: s = mid+1
    tmp2 = s
        
    if tmp1 <= tmp2:
        print(tmp1)
        print(min_x, min_y)
        print(max_x-tmp1, max_y-tmp1)
    else:
        print(tmp2)
        print(max_x-tmp2, min_y)
        print(min_x, max_y-tmp2)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()