import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline


def U(s, e, l, r, tree_idx, tree, count, val, ys):
    if s > r or e < l: return
    
    if s >= l and e <= r:
        count[tree_idx] += val
        
    else:
        mid = (s+e)>>1
        U(s, mid, l, r, tree_idx<<1, tree, count, val, ys)
        U(mid+1, e, l, r, tree_idx<<1|1, tree, count, val, ys)
        
    if count[tree_idx]:
        tree[tree_idx] = ys[e] - ys[s-1]
    else:
        if s == e: tree[tree_idx] = 0
        else: tree[tree_idx] = tree[tree_idx<<1] + tree[tree_idx<<1|1]


def solve():
    
    coordinates = []
    
    N = int(input())
    
    for _ in range(N):
        coordinates.append(tuple(map(int, input().split())))
    
    xs = list()
    ys = set()
    for x1, x2, y1, y2 in coordinates:
        xs.append((x1, y1, y2, 1))
        xs.append((x2, y1, y2, -1))
        ys.add(y1)
        ys.add(y2)

    xs.sort()    
    ys = list(ys)
    ys.sort()
    
    y_to_cnt = {}
    cnt = 0
    for y in ys:
        cnt += 1
        y_to_cnt[y] = cnt
        
    tree = [0] * (4 * cnt + 1)
    count = [0] * (4 * cnt + 1)
    
    ans = 0
    
    prev, y1, y2, _ = xs[0]
    
    U(1, cnt-1, y_to_cnt[y1], y_to_cnt[y2]-1, 1, tree, count, 1, ys)
    
    for idx in range(1, len(xs)):
        x, y1, y2, flag = xs[idx]
        
        ans += (x - prev) * tree[1]
        prev = x
        U(1, cnt-1, y_to_cnt[y1], y_to_cnt[y2]-1, 1, tree, count, flag, ys)
        
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()