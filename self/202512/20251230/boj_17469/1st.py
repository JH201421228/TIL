import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def find(idx, tree):
    root = idx
    
    while root != tree[root]: root = tree[root]
    
    while root != idx:
        cur = idx
        idx = tree[idx]
        tree[cur] = root
        
    return root


def union(idx, tree, parent, sets):
    p = find(parent[idx], tree)
    tree[idx] = p
    
    if len(sets[p-1]) < len(sets[idx-1]): sets[p-1], sets[idx-1] = sets[idx-1], sets[p-1]
    
    sets[p-1].update(sets[idx-1])
    sets[idx-1].clear()
    
    return


def solve():
    N, Q = map(int, input().split())
    
    parent = [0, 1] + [int(input()) for _ in range(N-1)]
    
    sets = [set([int(input())]) for _ in range(N)]
    
    questions = [tuple(map(int, input().split())) for _ in range(N+Q-1)]
    
    tree = [i for i in range(N+1)]
    
    ans = []
    while questions:
        cur_questions = questions.pop()
        
        if cur_questions[0] == 1:
            union(cur_questions[1], tree, parent, sets)
        else:
            ans.append(len(sets[find(cur_questions[1], tree)-1]))
    
    ans = '\n'.join(list(map(str, reversed(ans))))

    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()