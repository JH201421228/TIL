import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


history = dict()


def dq(l, r):
    if l == r:
        return l
    
    mid = (l+r) >> 1
    l = dq(l, mid)
    r = dq(mid+1, r)
    
    print(f"? {l} {r}", flush=True)
    res = input().rstrip()
    
    if l in history:
        history[l].append(r)
    else:
        history[l] = [r]
        
    if r in history:
        history[r].append(l)
    else:
        history[r] = [l]
    
    if res == '>': return r
    else: return l


def dqq(l, r, idx):
    
    if l == r: return l
    
    mid = (l+r) >> 1
    l = dqq(l, mid, idx)
    r = dqq(mid+1, r, idx)
    
    print(f"? {history[idx][l]} {history[idx][r]}", flush=True)
    res = input().rstrip()
    
    if res == '>': return r
    else: return l


def solve():
    N = int(input())
    
    idx = dq(0, N-1)
    
    print('!', history[idx][dqq(0, len(history[idx]) - 1, idx)])
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()