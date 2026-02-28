import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


class Node:
    def __init__(self):
        self.cnt = 0
        self.l = -1
        self.r = -1


def cal(idx, depth, need, trie):
    if depth > 60: return depth - need + trie[idx].cnt
    
    if trie[idx].cnt <= need: return depth
    
    if trie[idx].l == -1: return cal(trie[idx].r, depth+1, need+1, trie)
    if trie[idx].r == -1: return cal(trie[idx].l, depth+1, need+1, trie)
    else: return max(cal(trie[idx].l, depth+1, max(1, need+1-trie[trie[idx].r].cnt), trie), cal(trie[idx].r, depth+1, max(1, need+1-trie[trie[idx].l].cnt), trie))


def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    
    trie = []
    trie.append(Node())
    
    for num in arr:
        idx = 0
        trie[idx].cnt += 1
        for i in range(61):
            if num & (1<<i):
                if trie[idx].r == -1:
                    trie[idx].r = len(trie)
                    trie.append(Node())
                idx = trie[idx].r
            else:
                if trie[idx].l == -1:
                    trie[idx].l = len(trie)
                    trie.append(Node())
                idx = trie[idx].l
            trie[idx].cnt += 1
                
    print(cal(0, 0, 0, trie))
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()