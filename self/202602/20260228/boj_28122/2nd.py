import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def cal(idx, depth, need, cnt, left, right):
    if depth > 60: return depth - need + cnt[idx]
    
    if cnt[idx] <= need: return depth
    
    if left[idx] == -1: return cal(right[idx], depth+1, need+1, cnt, left, right)
    if right[idx] == -1: return cal(left[idx], depth+1, need+1, cnt, left, right)
    else: return max(cal(left[idx], depth+1, max(1, need+1-cnt[right[idx]]), cnt, left, right), cal(right[idx], depth+1, max(1, need+1-cnt[left[idx]]), cnt, left, right))


def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    
    cnt, left, right = [0], [-1], [-1]
    
    for num in arr:
        idx = 0
        cnt[idx] += 1
        for i in range(61):
            if num & (1<<i):
                if right[idx] == -1:
                    right[idx] = len(cnt)
                    cnt.append(0)
                    left.append(-1)
                    right.append(-1)
                idx = right[idx]
            else:
                if left[idx] == -1:
                    left[idx] = len(cnt)
                    cnt.append(0)
                    left.append(-1)
                    right.append(-1)
                idx = left[idx]
            cnt[idx] += 1
                
    print(cal(0, 0, 0, cnt, left, right))
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()