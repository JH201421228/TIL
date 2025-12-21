import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline



def recur(n, trie):
    _trie = sorted(trie)
    for c in _trie:
        print('-' * 2*n, c, sep='')
        recur(n+1, trie[c])



def solve():
    N = int(input())
    
    trie = {}
    
    for _ in range(N):
        info = list(input().rstrip().split())
        
        cur = trie
        
        for i in info[1:]:
            if i not in cur: cur[i] = {}
            cur = cur[i]
            
    recur(0, trie)
        
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()