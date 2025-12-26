import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def find(idx, tree):
    if idx == tree[idx]: return idx
    
    tree[idx] = find(tree[idx], tree)
    
    return tree[idx]


def union(idx, tree, parent):
    p = find(parent[idx], tree)
    
    tree[idx] = p
    
    return


def solve():
    N, Q = map(int, input().split())
    
    parent = [0, 1]
    for _ in range(N-1): parent.append(int(input()))
    
    question = [tuple(map(int, input().split())) for _ in range(Q+N-1)]

    tree = [i for i in range(N+1)]
    ans = ""

    while question:
        cur_question = question.pop()
        
        if cur_question[0]:
            if find(cur_question[1], tree) == find(cur_question[2], tree):
                ans = "YES\n" + ans
            else:
                ans = "NO\n" + ans
                
        else:
            union(cur_question[1], tree, parent)
            
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()