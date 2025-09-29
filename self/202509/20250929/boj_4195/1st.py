import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def find_parent(n, parent):
    if parent[n] == n: return n
    return find_parent(parent[n], parent)


def union_parent(n, m, parent, parent_size):
    n_p = find_parent(n, parent)
    m_p = find_parent(m, parent)

    if n_p < m_p:
        parent[m] = n_p
        parent_size[n_p] += parent_size[m_p]
        parent_size[m_p] = 0
        return n_p
    else:
        parent[n] = m_p
        parent_size[m_p] += parent_size[n_p]
        parent_size[n_p] = 0
        return m_p


def solve():
    name_to_num = {}
    rel = int(input())
    parent = [i for i in range(rel*2+1)]
    parent_size = [1] * (rel*2+1)
    cur = 0
    
    for _ in range(rel):
        names = tuple(input().rstrip().split())
        for name in names:
            if name in name_to_num: continue
            cur += 1
            name_to_num[name] = cur
            
        p = union_parent(name_to_num[names[0]], name_to_num[names[1]], parent, parent_size)

        print(parent_size[p])

    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()